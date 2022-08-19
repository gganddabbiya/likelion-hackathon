// 페이지네이션
function movePage(page) {
    const URLSearch = new URLSearchParams(location.search);
    URLSearch.set('page', String(page));
};
//날짜 변경시 url 바뀌는거 
// 달력 value 값 가져오기
$("#calendarInput").on("propertychange change keyup paste input", function() {
    var date = $('#calendarInput').val();

    var splitDate = date.split(' - ');
    
    var newStartDate = splitDate[0];
    var newEndDate = splitDate[1];
    
    var url = window.location.href;
    
    url.searchParams.set('startDate', newStartDate);
    url.searchParams.set('endDate', newEndDate);
});
