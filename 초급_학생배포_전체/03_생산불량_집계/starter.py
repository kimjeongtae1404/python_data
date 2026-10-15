import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)
        return rows

def save_csv(path, rows, columns):
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

TOPIC = 3
KEY = 'record_id'
COLUMNS = ['record_id', 'production_date', 'equipment_name', 'product_name', 'produced_qty', 'good_qty', 'defect_qty']

record=[]
count_dict={}
raw=[]
class Manager:
    def __init__(self):
        self.raw_rows = []
        self.valid_rows = []
        self.error_rows = []

    def load_data(self):
        self.raw_rows = []
        for path in sorted((ROOT / "data").glob("*.csv")):
            for number, row in enumerate(read_csv(path), 2):
                row["source_file"] = path.name
                row["source_line"] = number
                self.raw_rows.append(row)



    def validate_data(self):
        self.valid_rows = []
        self.error_rows = []
        seen_ids = set()

        for row in self.raw_rows:
        
            
            key=row.get('record_id')
            count_dict[key] = count_dict.get(key, 0) + 1

            

            if int(count_dict.get(key))>1:
                continue
                
            else:

                raw.append(row)

     
        print(raw)

        print(f"검사 완료: 정상 {len(self.valid_rows)}건, 오류 {len(self.error_rows)}건")

    def summarize_data(self):
        # TODO: 딕셔너리로 그룹별 합계를 계산하세요.
        raise NotImplementedError("집계 기능을 구현하세요")

    def save_results(self):
        # TODO: results 폴더 생성 후 save_csv 함수를 활용하세요.
        raise NotImplementedError("결과 저장 기능을 구현하세요")

if __name__ == "__main__":
    manager = Manager()
    manager.load_data()
    print(manager.raw_rows)
    manager.validate_data()


    
    print("읽은 행 수:", len(manager.raw_rows))
    print("첫 번째 행:", manager.raw_rows[36] if manager.raw_rows else "데이터 없음")
    print("읽기 기능만 완성된 시작 코드입니다. 나머지 기능을 구현하세요.")

    