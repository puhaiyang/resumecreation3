// webpack.config.js
const path = require('path');

module.exports = {
    // 其他配置项
    entry: './empty.js', // 你的入口文件
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, './frontend'),
    },
    devServer: {
        static: {
            directory: path.join(__dirname, './frontend'), // 用于服务静态文件
        },
        compress: true,
        port: 9000, // 你想要的端口
        proxy: [
            {
                context: ['/api'], // 需要被代理的路径
                target: 'http://localhost:8000', // 你的后端 API 地址
                changeOrigin: true, // 对于虚拟托管的站点，需要这个设置
                pathRewrite: {
                    '^/api': '', // 如果需要重写路径，可以添加此项
                },
            },
        ],
    },
};
