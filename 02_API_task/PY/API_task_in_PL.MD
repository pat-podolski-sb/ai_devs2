
Zaliczone zadania

 C01L01 (próba: 1)  [2024-03-18 15:37:48]
Zadania API

Zadania prompt

Quizy
Niezaliczone zadania API: helloapi

Niezaliczone zadania z promptem: getinfo

Informacje ogólne

TWÓJ API KEY:
c932421f
API zawsze odpowiada w formacie JSON
Kod błedu 0 (zero) oznacza zaliczone zadanie
Ujemne kody błędów to errory (ich wyjaśnienie jest w polu 'msg')
Od pobrania pytania, na udzielenie odpowiedzi masz 120 sekund
Autoryzacja

W celu zdobycia tokena uwierzytelniającego wyślij metodą POST poniższe dane do zasobu /token/TASKNAME

{
  "apikey": "c932421f"
}
Przykład:

Wielkość liter w hashu i nazwie zadanie nie ma znaczenia.

Uwaga: token jest jednorazowy. Musisz go pobrać przed każdym podejściem do zadania

Pobranie zadania (dane wejściowe)

Wyślij zapytanie typu GET do zasobu /task/TOKEN

Przykład:

curl https://tasks.aidevs.pl/task/e1fea75a
Token to ciąg znaków uzyskanych w kroku "autoryzacja".

Zgłaszanie odpowiedzi

Wyślij metodą POST dane o poniższym formacie do zasobu /answer/TOKEN

{
  "answer": "tutaj wpisujesz odpowiedz"
}
Przykład:

curl -d '{ "answer": "tutaj wpisujesz odpowiedz" }' https://tasks.aidevs.pl/answer/e1fea75
Uwaga: na zgłoszenie odpowiedzi masz tylko 120 sekund od czasu pobrania zadania

Zadanie testowe

Używając swojego klucza API, rozwiąż zadanie o nazwie HelloAPI

Zadanie polega na pobraniu zmiennej cookie z powyższego taska i odesłaniu jej do serwera jako odpowiedzi w polu answer (w JSON)

W razie problemu z zadaniami, pamiętaj o naszej społeczności
