import pandas as pd

# 레벤슈타인 거리 계산 함수
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    # s2가 비어있다면, s1의 길이가 거리
    if len(s2) == 0:
        return len(s1)

    previous_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

class LevenshteinChatBot:
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)
    
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()
        answers = data['A'].tolist()
        return questions, answers

    def find_best_answer(self, input_sentence):
        distances = [levenshtein_distance(input_sentence, q) for q in self.questions]
        best_match_index = distances.index(min(distances))
        return self.answers[best_match_index]

# CSV 파일 경로 #그냥 filepayh=filepath = 'ChatbotData.csv' 사용시 경로의 파일을 찾지못해 상시경로로 수정
filepath = r'c:\Users\sksms\Downloads\새 폴더\ChatbotData.csv' 

# 챗봇 인스턴스 생성
chatbot = LevenshteinChatBot(filepath)

# 챗봇과 대화
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)