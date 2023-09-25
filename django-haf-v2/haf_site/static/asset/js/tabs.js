function openCity(event, cityName) {
    var tabcontent = document.getElementsByClassName("tabcontent");
    var tablinks = document.getElementsByClassName("tablinks");

    // Tüm tab içeriklerini gizle
    for (var i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Tüm menüleri etkin olmayan hale getir
    for (var i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active-menu");
    }

    // Seçilen menüyü aktif hale getir
    var selectedTab = document.getElementById(cityName);
    selectedTab.style.display = "block";

    // Seçilen menüyü aktif hale getir
    event.currentTarget.classList.add("active-menu");
}

document.addEventListener("DOMContentLoaded", function () {
    openCity(event, 'All');
});