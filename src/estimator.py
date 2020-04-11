import math

region = {
    "name":"Africa",
    "avgAge":19.7,
    "avgDailyIncomeInUSD": 4,
    "avgDailyIncomePopulation":0.73
}


periodType = "days"
timeToElapse = 38
reportedCases = 2747
population = 92931687
totalHospitalBeds = 678874

data = {
    "region":region,
    "periodType":periodType,
    "timeToElapse":timeToElapse,
    "reportedCases":reportedCases,
    "population":population,
    "totalHospitalBeds":totalHospitalBeds
}


def timeFrame(data):
  period = data["periodType"]
  value = data["timeToElapse"]
  if period == "months":
    value = value * 30
  elif period == "weeks":
    value = value * 7
  else:
    value = data["timeToElapse"]
  return value



def infectionTime(data, currentlyInfected):
    valueTime = (timeFrame(data))/3
    integralPeriod = math.trunc(valueTime)
    period = math.trunc(currentlyInfected * (2**integralPeriod))
    return period




def severeCases(infectionsByRequestedTime):
  cases = round(0.15 * infectionsByRequestedTime)
  return cases

def requestedBeds(data, severeCasesByRequestedTime):
  totalSevereBeds = 0.35 * data["totalHospitalBeds"]
  cases = math.trunc(totalSevereBeds - severeCasesByRequestedTime)
  return cases

def icuRequestTime(infectionsByRequestedTime):
  cases = 0.05 * infectionsByRequestedTime
  cases = math.trunc(cases)
  return cases

def ventilatorRequestTime(infectionsByRequestedTime):
  cases = 0.02 * infectionsByRequestedTime
  cases =math.trunc(cases)
  return cases

def moneySpent(data, infectionsByRequestedTime):
  dataRegions = data['region']
  avgIncome = dataRegions['avgDailyIncomeInUSD']
  avgIncomePopulation = dataRegions['avgDailyIncomePopulation']
  period = timeFrame(data)
  value = (avgIncome * avgIncomePopulation * infectionsByRequestedTime)/period
  amount = math.trunc(value)
  return amount








def normalImpact(data):
    currentlyInfected = data['reportedCases'] * 10
    infectionsByRequestedTime = infectionTime(data, currentlyInfected)
    severeCasesByRequestedTime = severeCases(infectionsByRequestedTime)
    hospitalBedsByRequestedTime = requestedBeds(data, severeCasesByRequestedTime)
    casesForICUByRequestedTime = icuRequestTime(infectionsByRequestedTime)
    casesForVentilatorsByRequestedTime = ventilatorRequestTime(infectionsByRequestedTime)
    dollarsInFlight = moneySpent(data, infectionsByRequestedTime)

    data = {
        "currentlyInfected":currentlyInfected,
        "infectionsByRequestedTime":infectionsByRequestedTime,
        "severeCasesByRequestedTime":severeCasesByRequestedTime,
        "hospitalBedsByRequestedTime": hospitalBedsByRequestedTime,
        "casesForICUByRequestedTime": casesForICUByRequestedTime,
        "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTime,
        "dollarsInFlight":dollarsInFlight
    }
    
    return data

def worseImpact(data):
    currentlyInfected = data['reportedCases'] * 50
    infectionsByRequestedTime = infectionTime(data, currentlyInfected)
    severeCasesByRequestedTime = severeCases(infectionsByRequestedTime)
    hospitalBedsByRequestedTime = requestedBeds(data, severeCasesByRequestedTime)
    casesForICUByRequestedTime = icuRequestTime(infectionsByRequestedTime)
    casesForVentilatorsByRequestedTime = ventilatorRequestTime(infectionsByRequestedTime)
    dollarsInFlight = moneySpent(data, infectionsByRequestedTime)


    data = {
        "currentlyInfected":currentlyInfected,
        "infectionsByRequestedTime": infectionsByRequestedTime,
        "severeCasesByRequestedTime":severeCasesByRequestedTime,
        "hospitalBedsByRequestedTime": hospitalBedsByRequestedTime,
        "casesForICUByRequestedTime": casesForICUByRequestedTime,
        "casesForVentilatorsByRequestedTime": casesForVentilatorsByRequestedTime,
        "dollarsInFlight": dollarsInFlight
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