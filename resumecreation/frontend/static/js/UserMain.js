// js/main.js
document.addEventListener("DOMContentLoaded", function() {
    // 动态加载 navbar.html
    var navbarContainer = document.getElementById('navbar');
    fetch('../static/html/UserNavBar.html')
        .then(response => response.text())
        .then(data => {
            navbarContainer.innerHTML = data; // 将导航栏 HTML 插入到页面中
        })
        .catch(error => console.error('Error loading navbar:', error));

    // 动态加载 footer.html
    var footerContainer = document.getElementById('footer');
    fetch('../static/html/UserBottomBar.html')
        .then(response => response.text())
        .then(data => {
            footerContainer.innerHTML = data; // 将页脚 HTML 插入到页面中
        })
        .catch(error => console.error('Error loading footer:', error));

    // 动态加载 sidebar.html
    // var sidebarContainer = document.getElementById('sidebar');
    // fetch('../static/html/UserSideBar.html')
    //     .then(response => response.text())
    //     .then(data => {
    //         sidebarContainer.innerHTML = data; // 将页脚 HTML 插入到页面中
    //     })
    //     .catch(error => console.error('Error loading sidebar:', error));
});
