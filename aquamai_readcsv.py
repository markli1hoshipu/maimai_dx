from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

if __name__ == "__main__":

    # main_web = "https://aquadx.net/home"
    # main_web = "https://aquadx.net/ranking"
    main_web = "https://aquadx.net/u/hoshipu1/mai2"

    # username = "marklizhiyuan@outlook.com"
    # password = "681206Lk@"

    wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
    wd.implicitly_wait(15)

    wd.get(main_web)   # 打开初始界面

    song_titles = wd.find_elements(By.XPATH, "//div[contains(@class, 'song-title')]")
    levels      = wd.find_elements(By.XPATH, "//span[contains(@class, 'lv')]")
    ranks       = wd.find_elements(By.XPATH, "//span[contains(@class, 'rank-text')]")
    scores      = wd.find_elements(By.XPATH, "//span[contains(@class, 'rank-num')]")
    ratings     = wd.find_elements(By.XPATH, "//span[contains(@class, 'dx-change')]")

    # for i in range(len(song_titles)):
    #     print(f"歌曲 {i + 1}:")
    #     print(f"  歌曲标题: {song_titles[i].text}")
    #     print(f"  等级: {levels[i].text}")
    #     print(f"  百分比: {ranks[i].text}")
    #     print(f"  DX 改变值: {scores[i].text}")
    #     print(f"  DX 改变值: {ratings[i].text}")
    #     print("-" * 30)

    # 初始化一个空列表，用于保存提取的数据
    data = []

    # 遍历所有歌曲信息并保存到列表
    for i in range(len(song_titles)):
        song_data = {
            "歌曲标题": song_titles[i].text,
            "等级": levels[i].text,
            "百分比": ranks[i].text,
            "得分": scores[i].text,
            "DX 改变值": ratings[i].text
        }
        data.append(song_data)

    # 将数据转换为 Pandas DataFrame
    df = pd.DataFrame(data)

    # 保存到 Excel 文件
    df.to_excel("歌曲信息.xlsx", index=False)

    # 打印保存成功的提示
    print("数据已成功保存到歌曲信息.xlsx")
    time.sleep(60)
    # 关闭浏览器
    wd.quit()