region = {
    "name":"Africa",
    "avgAge":19.7,
    "avgDailyIncomeInUSD": 2,
    "avgDailyIncomePopulation":0.71
}

periodType = "days"
timeToElapse = 58
reportedCases = 674
population = 66622705
totalHospitalBeds = 1380614

data = {
    "region":region,
    "periodType":periodType,
    "timeToElapse":timeToElapse,
    "reportedCases":reportedCases,
    "population":population,
    "totalHospitalBeds":totalHospitalBeds
}

def infectionTime(data, currentlyInfected):
    integralPeriod = int((data['timeToElapse'])/3)
    period = currentlyInfected * (2**integralPeriod)
    return period

def normalImpact(data):
    currentlyInfected = data['reportedCases'] * 10
    infectionsByRequestedTime = infectionTime(data, currentlyInfected)
    data = {
        "currentlyInfected":currentlyInfected,
        "infectionsByRequestedTime":infectionsByRequestedTime,
    }
    
    return data

def worseImpact(data):
    currentlyInfected = data['reportedCases'] * 50
    infectionsByRequestedTime = infectionTime(data, currentlyInfected)
    data = {
        "currentlyInfected":currentlyInfected,
        "infectionsByRequestedTime": infectionsByRequestedTime
    }
    
    return data


def estimator(data):
  severeImpact = worseImpact(data)
  impact = normalImpact(data)
      
      
  data = {
      "data":data,
      "impact":impact,
      "severeImpact": severeImpact
    }
  print(data)

  return data

estimator(data)