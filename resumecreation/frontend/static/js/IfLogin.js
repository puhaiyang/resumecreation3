import { CONFIG } from "./config.js";  // 导入配置


// Load this script in the HTML file to check if the user is logged in
    // 在页面加载时使用 AJAX 请求检查用户的登录状态
    document.addEventListener("DOMContentLoaded", function() {
        var userNav = document.getElementById('user-nav');

        // 通过 AJAX 检查登录状态
        function checkAuthentication() {
            fetch(`${CONFIG.API_URL}/check-auth/`, {

                method: 'GET',
                credentials: 'include' // 包含 cookie 信息
            })
            .then(response => response.json())
            .then(data => {
                if (data.is_authenticated) {
                    // 如果用户已登录，动态生成用户菜单
                    var username = data.username;
                    userNav.innerHTML = `
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                ${username}
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="userDropdown">
                                <li><a class="dropdown-item" href="user/UserHome.html">Home</a></li>
                                <li><a class="dropdown-item" href="user/UserProfile.html">Profile</a></li>
                                <li><a class="dropdown-item" href="user/Logout.html">Logout</a></li>
                            </ul>
                        </li>
                    `;
                } else {
                    // 如果用户未登录，显示登录/注册菜单
                    userNav.innerHTML = `
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="authDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Login/Sign Up
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="authDropdown">
                                <li><a class="dropdown-item" href="login.html">Login</a></li>
                                <li><a class="dropdown-item" href="register.html">Sign Up</a></li>
                            </ul>
                        </li>
                    `;
                }
            })
            .catch(error => {
                console.error('Error checking authentication:', error);
            });
        }

        // 调用函数检查登录状态
        checkAuthentication();
    });

