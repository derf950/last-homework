import csv

class input:
    def rdrfile1(self):  #csv 파일을 읽어와 리스트로 변환
        with open('커피자료1.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.How = [line for line in csv_reader]
            self.How = self.How[1:]

    def rdrfile2(self):  # csv 파일을 읽어와 리스트로 변환
        with open('방식자료1.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.How = [line for line in csv_reader]
            self.How = self.How[1:]

    def hobby(self, a): #불러온 파일의 정보를 사용자가 입력한 정보를 토대로 정보를 추출하는 함수 /a: 카테고리 숫자 /
        y = self.How[a][0]
        n = input(y+"을(를) 얼마나 원하시나요?(1:연함/2:중간/3:진함")
        coffee_list = []
        for x in self.How:
            for b in self.How:
                self.How[a][b]
                for b in self.How[a][b]:
                    if self.How[a][b] == n:
                        coffee_list.extend(b)
                    b += 1
        return (coffee_list)

    def preference(self,list): #추출한 정보를 한 리스트로 취합하여 리스트 내 카테고리의 갯수를 세어 2개 이상으로 확인되는 코드의 제목을 표출한다
        if p in list:
            cunt = int(list.count(p))
            if cunt > 2:
                print(self.How[cunt][0])

class output:

    def resultout(self,result):#코드의제목을 받아 그 정보를 포함한 csv파일을 실행시켜서 사용자에게 추천하는 커피와 추출방식을 표출한다.
        with open(self.f_csv, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            result_list = [line for line in csv_reader]
            result_list = result_list[1:]

            print(result_list[result][0])
            print(result_list[result][1])

if __name__ == "__main__":
    coffeefavorit = input
    output_list = []
    for u in range(1,4):
        output_list.extend(coffeefavorit.hobby(u).coffee_list)

    coffeefavorit.preference(output_list)



