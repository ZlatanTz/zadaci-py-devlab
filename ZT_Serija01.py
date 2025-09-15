# 18 zadatak, 23 zadatak, 39 zadatak, 96 zadatak

def checkWaterState(temp: int) -> str:
  try:
    if(temp > 100):
      return 'cvrsto'
    if(temp < 0):
      return 'gasovito'
    return 'tecno'
    
  except TypeError:
    return 'unesite broj'
    

print(checkWaterState('a'))

def checkCoordinates(x: float, y: float) -> bool:
  try:
    udaljenost_kvadrat = x**2 + y**2
    u_prstenu = 16 <= udaljenost_kvadrat <= 36

    u_poluravni = (x - y - 4) <= 0

    if u_prstenu and u_poluravni:
        return True
    else:
        return False
  except TypeError:
    return 'unesite brojeve'
  

def isNarcisNum(num: int) -> bool:
    try:
      digits = str(num)
      power = len(digits)
      total = sum(int(d)**power for d in digits)
      return total == num
    except TypeError:
       return 'unesi broj'

print(isNarcisNum(151))

def split_string(s: str, x: int) -> list[str]:
    result = []
    try:
        for i in range(0, len(s), x):
            chunk = s[i:i+x]
            if len(chunk) < x:
                chunk += '*' * (x - len(chunk))
            result.append(chunk)
        return result
    except TypeError:
        print('nevalidno uneseni podaci')
        return []



   

    



