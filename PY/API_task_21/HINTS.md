1) Send the URL to your own API to /answer/ endpoint in the following format:

{
 "answer":"https://anything.you.want.com/v1/some/api/whatever"}
}

_____________________________________

2) Our system will send question to Your API via the provided URL and POST method. We will send JSON:

{
 "question":"give me URL to polish portal called Onet"
}



_____________________________________

3) Your system has to answer in the provided format:

{
 "reply":"this is the answer to our question"
}

IMPORTANT: answer is always an URL. Do not send whole HTML code or sentence

_____________________________________

P.S. You will sometimes get 'tricky' questions that can break JSON format - be prepared!

Zadania praktyczne

Rozwiąż zadanie API o nazwie ‘google’. Do jego wykonania będziesz potrzebować darmowego konta w usłudze SerpAPI. Celem zadania jest samodzielne zaimplementowanie rozwiązania podobnego do tego, znanego z ChatGPT Plus, gdzie po wpisaniu zapytania na temat, o którym model nie ma pojęcia, uruchamiana jest wyszukiwarka BING. My posłużymy się wyszukiwarką Google, a Twój skrypt będzie wyszukiwał odpowiedzi na pytania automatu sprawdzającego i będzie zwracał je w czytelnej dla człowieka formie. Więcej informacji znajdziesz w treści zadania /task/, a podpowiedzi dostępne są pod https://tasks.aidevs.pl/hint/google.