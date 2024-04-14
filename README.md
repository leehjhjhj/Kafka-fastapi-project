# 😸🇰🇷🇯🇵 코오자프로젝트(개발중)
<img src="https://github.com/leehjhjhj/Kafka-fastapi-project/assets/102458609/5514f776-019b-4954-add1-3f8faa640e7e" width="200" height="200">

## 소개
카프카를 활용한 한국-일본 뉴스 서비스 만들기
- 일본 뉴스과 한국 뉴스를 크롤링
- 크롤링하여 fastapi에 구현된 프로듀서에 전송
- `raw.articles` 토픽에서 이를 소비하여 제목에 ‘韓国’, ‘韓’, ‘일본’, ‘日’ 등의 키워드를 필터링
- 그리고 `article.transation.requests` 토픽으로 보냄. 이를 TraslatingConsumer가 소비
- Amazon translate로 번역을 각각하고 `article.saving.requests` 토픽으로 전송
- 이를 SavingConsumer가 소비하고 데이터베이스에 저장시킴
- 공통된 한일 이슈에 대해서 서로 어떻게 기사가 나가는지 한 눈에 볼 수 있으며, 번역을 통해서 학습 효과까지 노려봄

## 아키텍처
![코오자-아키텍처](https://github.com/leehjhjhj/Kafka-fastapi-project/assets/102458609/095551cb-e216-4e33-8708-51d94014ae6c)
