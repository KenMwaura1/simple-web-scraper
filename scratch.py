try:
        social:
    except social[0] == '':
        pass
    social = tr.find_all("td")[3].find("div").find("ul").find_all("li")[0]
    if social :
        pass
    else:
        social = "pass"