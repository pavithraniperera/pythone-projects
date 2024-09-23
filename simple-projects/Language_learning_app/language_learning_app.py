import random
words = [
    {"Korean": "안녕하세요", "English": "Hello"},
    {"Korean": "감사합니다", "English": "Thank you"},
    {"Korean": "사랑해요", "English": "I love you"},
    {"Korean": "미안해요", "English": "I'm sorry"},
    {"Korean": "잘 지냈어요?", "English": "How are you?"},
    {"Korean": "네", "English": "Yes"},
    {"Korean": "아니요", "English": "No"},
    {"Korean": "좋아요", "English": "Good"},
    {"Korean": "나쁜", "English": "Bad"},
    {"Korean": "어디에요?", "English": "Where is it?"},
    {"Korean": "얼마에요?", "English": "How much is it?"},
    {"Korean": "이름", "English": "Name"},
    {"Korean": "나이", "English": "Age"},
    {"Korean": "물", "English": "Water"},
    {"Korean": "음식", "English": "Food"},
    {"Korean": "학교", "English": "School"},
    {"Korean": "친구", "English": "Friend"},
    {"Korean": "집", "English": "House"},
    {"Korean": "가족", "English": "Family"},
    {"Korean": "행복", "English": "Happiness"},
    {"Korean": "돈", "English": "Money"},
    {"Korean": "병원", "English": "Hospital"},
    {"Korean": "의사", "English": "Doctor"},
    {"Korean": "약", "English": "Medicine"},
    {"Korean": "시간", "English": "Time"},
    {"Korean": "날씨", "English": "Weather"},
    {"Korean": "여행", "English": "Travel"},
    {"Korean": "비행기", "English": "Airplane"},
    {"Korean": "자동차", "English": "Car"},
    {"Korean": "버스", "English": "Bus"},
    {"Korean": "지하철", "English": "Subway"},
    {"Korean": "기차", "English": "Train"},
    {"Korean": "비행기표", "English": "Plane ticket"},
    {"Korean": "여권", "English": "Passport"},
    {"Korean": "비자", "English": "Visa"},
    {"Korean": "경찰", "English": "Police"},
    {"Korean": "운동", "English": "Exercise"},
    {"Korean": "음악", "English": "Music"},
    {"Korean": "영화", "English": "Movie"},
    {"Korean": "책", "English": "Book"},
    {"Korean": "컴퓨터", "English": "Computer"},
    {"Korean": "핸드폰", "English": "Cell phone"},
    {"Korean": "인터넷", "English": "Internet"},
    {"Korean": "가게", "English": "Store"},
    {"Korean": "시장", "English": "Market"},
    {"Korean": "쇼핑", "English": "Shopping"},
    {"Korean": "옷", "English": "Clothes"},
    {"Korean": "구두", "English": "Shoes"},
    {"Korean": "안경", "English": "Glasses"},
    {"Korean": "모자", "English": "Hat"},
    {"Korean": "카페", "English": "Cafe"},
    {"Korean": "커피", "English": "Coffee"},
    {"Korean": "차", "English": "Tea"},
    {"Korean": "빵", "English": "Bread"},
    {"Korean": "과일", "English": "Fruit"},
    {"Korean": "야채", "English": "Vegetables"},
    {"Korean": "고기", "English": "Meat"},
    {"Korean": "밥", "English": "Rice"},
    {"Korean": "국수", "English": "Noodles"},
    {"Korean": "김치", "English": "Kimchi"},
    {"Korean": "불고기", "English": "Bulgogi"},
    {"Korean": "비빔밥", "English": "Bibimbap"},
    {"Korean": "된장찌개", "English": "Doenjang jjigae"},
    {"Korean": "물고기", "English": "Fish"},
    {"Korean": "닭", "English": "Chicken"},
    {"Korean": "돼지고기", "English": "Pork"},
    {"Korean": "소고기", "English": "Beef"},
    {"Korean": "맥주", "English": "Beer"},
    {"Korean": "와인", "English": "Wine"},
    {"Korean": "술", "English": "Alcohol"},
    {"Korean": "냉장고", "English": "Refrigerator"},
    {"Korean": "텔레비전", "English": "Television"},
    {"Korean": "침대", "English": "Bed"},
    {"Korean": "의자", "English": "Chair"},
    {"Korean": "책상", "English": "Desk"},
    {"Korean": "창문", "English": "Window"},
    {"Korean": "문", "English": "Door"},
    {"Korean": "벽", "English": "Wall"},
    {"Korean": "바닥", "English": "Floor"},
    {"Korean": "천장", "English": "Ceiling"},
    {"Korean": "화장실", "English": "Bathroom"},
    {"Korean": "거실", "English": "Living room"},
    {"Korean": "주방", "English": "Kitchen"},
    {"Korean": "침실", "English": "Bedroom"},
    {"Korean": "식탁", "English": "Dining table"},
    {"Korean": "물건", "English": "Thing"},
    {"Korean": "음식점", "English": "Restaurant"},
    {"Korean": "공항", "English": "Airport"},
    {"Korean": "호텔", "English": "Hotel"},
    {"Korean": "도서관", "English": "Library"},
    {"Korean": "박물관", "English": "Museum"},
    {"Korean": "약국", "English": "Pharmacy"},
    {"Korean": "우체국", "English": "Post office"},
    {"Korean": "은행", "English": "Bank"},
    {"Korean": "편의점", "English": "Convenience store"},
    {"Korean": "슈퍼마켓", "English": "Supermarket"},
    {"Korean": "공원", "English": "Park"},
]

def quiz_user(words):
    random.shuffle(words)
    score=0
    for word in words:
        print(f"what is the english translate of this korean word {word['Korean']}")
        user_answer = input("Type your answer here : ").strip().lower()  
        correct_answer = word["English"].lower() 
        
        if user_answer==correct_answer:
            print("correct !!\n")
            score+=1
        else:
            print(f"your answer is wrong . Correct answer is {correct_answer}\n")
    print(f"your toatal score is {score}")

def main():
    print("WElcome to the language learning flashcard app !!\n")
    input("Press enter to start the quiz..! \n")
    quiz_user(words)

if __name__ =="__main__":
    main()