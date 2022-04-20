
from random import randrange
import utilities
import color_samples

sequence = ['yellow', 'cyan', 'green', 'red']
testData = color_samples.colorSamples
testDataColorOnly = color_samples.testColorOnlyData

def countColors(color,testData):
  count = 0
  for value in testData:
    if(value[1] == color):
      count += 1
  return count

#DO NOT CHANGE CODE ABOVE THIS LINE!

#To use noisier data, uncomment this line:
testData += color_samples.noisyColorSamples

#Your task is to write a function using Python that correctly returns a color based on the red, green, and blue values.

#The identifyColor function should return "red","yellow","cyan", or "green" based on the red, green, and blue values. These values are numbers between 0 - 255.

#Your task is to write this function to correctly identify which of the four colors is represented by the three inputs. 

def identifyColor(colorValues):
  red = colorValues[0]
  green = colorValues[1]
  blue = colorValues[2]

  if red <= 124: #green or cyan
    if blue <= 180:
      return "green"
    else:
      return "cyan"
  elif green <= 100:
    return "red"
  else:
    return "yellow"
    

#This next function is designed to figure out how many transitions from one color to the next have occured as the color wheel rotates. One complete rotation should involve eight transitions. 

def countTransitionsColorOnly(testDataColorOnly):
  numberOfTransitions = 0
  previousColor = "yellow"
  for color in testDataColorOnly:
    currentColor = color
    #Your code should go here. Watch the indentation of the code you put below as it should match this one.
    position = sequence.index(previousColor) + 1
    if position > 3:
      position = 0
        
    if previousColor != currentColor:
      if sequence[position] == currentColor:
        numberOfTransitions += 1
      else:
        quit()
        pass

    previousColor = currentColor
  #Your final answer should be stored in the variable called numberOfTransitions.
  return numberOfTransitions
  


def countTransitions(testData):
  numberOfTransitions = 0
  previousColor = "yellow"
  for value in testData:
    currentColor = identifyColor(value[0])
    #Your code should go here. Watch the indentation of the code you put below as it should match this one.
    
    position = sequence.index(previousColor) + 1
    if position > 3:
      position = 0
        
    if previousColor != currentColor:
      if sequence[position] == currentColor:
        numberOfTransitions += 1
      else:
        quit()
        pass

    previousColor = currentColor

  #Your final answer should be stored in the variable called numberOfTransitions.
  return numberOfTransitions


def testFunction():
  
  redCorrect = 0
  greenCorrect = 0
  yellowCorrect = 0
  cyanCorrect = 0
  for value in testData:
    if(identifyColor(value[0])==value[1]):
      if(value[1] == 'red'):
        redCorrect += 1
      elif(value[1] == 'green'):
        greenCorrect +=1
      elif(value[1] == 'yellow'):
        yellowCorrect += 1
      else:
        cyanCorrect += 1

  correctAnswers = redCorrect + greenCorrect + yellowCorrect + cyanCorrect
  print("Accuracy: {}% of the test data was classified correctly".format(round(correctAnswers*100.0/len(testData))))
  print("{} % of the red data was classified correctly".format(round(redCorrect*100.0/countColors('red',testData),2)))
  print("{} % of the green data was classified correctly".format(round(greenCorrect*100.0/countColors('green',testData),2)))
  print("{} % of the yellow data was classified correctly".format(round(yellowCorrect*100.0/countColors('yellow',testData),2)))
  print("{} % of the cyan data was classified correctly".format(round(cyanCorrect*100.0/countColors('cyan',testData),2)))
  print("{} transitions counted".format(countTransitionsColorOnly(testDataColorOnly)))
  print("{} transitions using identification counted".format(countTransitions(testData)))
  print(f'{countTransitions(testData)/8} wheel rotations')


testFunction()

