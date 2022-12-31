Параметры запуска:
    >> main.py -t - получить статистику за все время
    >> main.py -t -day - получить статистику в течении дня
    >> main.py -t -month - получить статистику в течении месяца
    >> main.py -t -year - получить статистику в течении года


    >> main.py -u - получить статистику по пользователям
    >> main.py -b - получить статистику по браузерам
    >> main.py -p - получить статистику по платформам
    >> main.py -r - получить статистику по поисковым запросам и референсам

Вставьте следующий JS код себе на сайт.

<script>
  function getCookie(name) {
	let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
	return matches ? decodeURIComponent(matches[1]) : '-1';
}
    if (getCookie('user') === '-1'){
        document.cookie = "user=0";
    }
    let url = 'http://10.249.15.161:8000/' + getCookie('user');

    fetch(url)
        .then(response => response.text().then(v => {
            document.cookie = "user=" + v;
            console.log("user=" + v);
        }));
</script>