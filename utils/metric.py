from collections import Counter

class Metric(object):
    def __init__(self, id2label):
        self.id2label = id2label
        self.real_labels = []
        self.pred_labels = []
        self.correct_labels = []
        
    def compute(self, real_count, pred_count, correct_count):
        recall = 0 if real_count == 0 else (correct_count / real_count)
        precision = 0 if pred_count == 0 else (correct_count / pred_count)
        f1 = 0. if recall + precision == 0 else (2 * precision * recall) / (precision + recall)
        return recall, precision, f1

    def get_result(self):
        result = {}
        real_counter = Counter([item for item in self.real_labels])
        pred_counter = Counter([item for item in self.pred_labels])
        correct_counter = Counter([item for item in self.correct_labels])
        for label, count in real_counter.items():
            real_count = count
            pred_count = pred_counter.get(label, 0)
            correct_count = correct_counter.get(label, 0)
            recall, precision, f1 = self.compute(real_count, pred_count, correct_count)
            result[label] = {"Precision": round(precision, 4), 'Recall': round(recall, 4), 'F1': round(f1, 4)}
        real_total_count = len(self.real_labels)
        pred_total_count = len(self.pred_labels)
        correct_total_count = len(self.correct_labels)
        recall, precision, f1 = self.compute(real_total_count, pred_total_count, correct_total_count)
        result["Total"] = {"Precision": round(precision, 4), 'Recall': round(recall, 4), 'F1': round(f1, 4)}

        return result
    


    def update(self, real_labels, pred_labels):
        for real_label, pred_label in zip(real_labels, pred_labels):
            self.real_labels.append(real_label)
            self.pred_labels.append(pred_label)
            if real_label == pred_label:
                self.correct_labels.append(pred_label)


    def format_print(self, result):
        def print_item(entity, metric):
            if entity != "Total":
                print(f"Entity: {entity} - Precision: {metric['Precision']} - Recall: {metric['Recall']} - F1: {metric['F1']}")
            else:
                print(f"Total: Precision: {metric['Precision']} - Recall: {metric['Recall']} - F1: {metric['F1']}")

        print("\n")
        print_item("Total", result["Total"])
        for key in result.keys():
            if key == "Total":
                continue
            text_key = self.id2label[key]
            print_item(text_key, result[key])
        print("\n")

