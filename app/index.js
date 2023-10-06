const {app, BrowserWindow} = require('electron')
const {spawn} = require('child_process');
const process = require('process')
const path = require('path')


console.log(process.env.STARTUP_MODE)
// const devMode = (process.argv || []).indexOf('--dev') !== -1
console.log(process.argv)


console.log(`electron 入口文件 ${__dirname}`)

//如果是在打包环境下面这样启动
if (__dirname.indexOf(`.asar`) !== -1) {
    const serverDirPath = path.join(__dirname,'../server');
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
}

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800, height: 600
    })

    win.loadFile('index.html')
}

app.whenReady().then(() => {
    createWindow()
})
