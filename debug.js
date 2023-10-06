const {spawn} = require('child_process');
const process = require('process')
const path = require('path')
const fs = require('fs');


const base = `~/__code/__lab/__electron/electron-python-app/__dist/target/mac-arm64/electron-python-app.app/Contents/Resources/app.asar`;

console.log(`${path.join(base,'../server')}`)

const serverDirPath = path.join(base,'../server');
// console.log(fs.readdirSync(serverDirPath))
const pythonProcess = spawn(path.join(serverDirPath,'/app/app'))

// 监听Python应用程序的标准输出
pythonProcess.stdout.on('data', (data) => {
    console.log(`服务端日志：${data}`);
});

// 当Python应用程序退出时
pythonProcess.on('exit', (code) => {
    console.log(`服务端报错，错误码 :: ${code}`);
});

// 当Python应用程序退出时
pythonProcess.on('close', (code) => {
    console.log(`服务端关闭，错误码 :: ${code}`);
});