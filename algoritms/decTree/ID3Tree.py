# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 10:39:22 2018

@author: aoanng
"""
from math import log

## Создать набор данных
def createDataSet():
    """
         Создать набор данных
    """
    dataSet = [['Молодежь', 'Нет', 'Нет', 'Общие', 'Отклонить'],
                ['Молодежь', 'Нет', 'Нет', 'Хорошо', 'Отклонить'],
                ['Молодежь', 'Да', 'Нет', 'Хорошо', 'Согласие'],
                ['Молодежь', 'Да', 'Да', 'Общие', 'Согласие'],
                ['Молодежь', 'Нет', 'Нет', 'Общие', 'Отклонить'],
                ['Средний возраст', 'Нет', 'Нет', 'Общие', 'Отклонить'],
                ['Средний возраст', 'Нет', 'Нет', 'Хорошо', 'Отклонить'],
                ['Средний возраст', 'Да', 'Да', 'Хорошо', 'Согласие'],
                ['Средний возраст', 'Нет', 'Да', 'Очень хорошо', 'Согласие'],
                ['Средний возраст', 'Нет', 'Да', 'Очень хорошо', 'Согласие'],
                ['Пожилые люди', 'Нет', 'Да', 'Очень хорошо', 'Согласие'],
                ['Пожилые люди', 'Нет', 'Да', 'Хорошо', 'Согласие'],
                ['Пожилые люди', 'Да', 'Нет', 'Хорошо', 'Согласие'],
                ['Пожилые люди', 'Да', 'Нет', 'Очень хорошо', 'Согласие'],
                ['Пожилые люди', 'Нет', 'Нет', 'Общие', 'Отклонить'],
                ]
    featureName = ['Возраст', 'Иметь работу', 'Есть дом', 'Кредитный профиль']
    # Возвращает имя набора данных и каждого измерения
    return dataSet, featureName

## Разделить набор данных
def splitDataSet(dataSet,axis,value):
    """
         Разделение набора данных по заданным характеристикам
         : ось параметра: размер объекта, который разделяет набор данных
         : param value: значение функции
         : return: все экземпляры, которые соответствуют элементу (и автоматически удаляют этот элемент измерения)
    """

    # Проходить по каждой строке данных в dataSet
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis] # Удалить этот размерный элемент
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

## Расчет информационной энтропии
# Всегда вычислять неопределенность меток категорий
def calcShannonEnt(dataSet):
    """
         Вычислить энтропию Шеннона случайной величины Y в наборе обучающих данных
    :param dataSet:
    :return:
    """
    numEntries = len(dataSet) # Количество экземпляров
    labelCounts = {}
    for featVec in dataSet: # Обходить каждый экземпляр, считая частоту меток
        currentLabel = featVec[-1] # Указывает на последний столбец
        # Текущей метки нет в карте labelCounts, пусть labelCounts добавит метку
        if currentLabel not in labelCounts.keys(): 
            labelCounts[currentLabel] =0
        labelCounts[currentLabel] +=1

    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob,2) # log base 2
    return shannonEnt

## Рассчитать условную энтропию
def calcConditionalEntropy(dataSet,i,featList,uniqueVals):
    """
         Вычислить условную энтропию Y в условиях, заданных x_i
         : param dataSet: набор данных
         : параметр I: измерение I
         : param featList: список возможностей набора данных
         : param unqiueVals: набор функций набора данных
         : return: условная энтропия
    """
    ce = 0.0
    for value in uniqueVals:
        subDataSet = splitDataSet(dataSet,i,value)
        prob = len(subDataSet) / float(len(dataSet)) #Максимальная вероятность вероятности оценки
        ce += prob * calcShannonEnt(subDataSet) # ∑pH (Y | X = xi) Расчет условной энтропии 
    return ce

## Рассчитать прирост информации
def calcInformationGain(dataSet,baseEntropy,i):
    """
         Расчет получения информации
         : param dataSet: набор данных
         : param baseEntropy: информационная энтропия Y в наборе данных
         : параметр i: размерность объекта i
         : return: прирост информации g (dataSet | X_i) функции i в наборе данных
    """
    featList = [example[i] for example in dataSet] # Список возможностей измерения i
    uniqueVals = set(featList) # Заменить на collection-каждый элемент в коллекции не повторяется
    newEntropy = calcConditionalEntropy(dataSet,i,featList,uniqueVals)# Рассчитать условную энтропию,
    infoGain = baseEntropy - newEntropy # Получение информации = Информационная энтропия. Условная энтропия.
    return infoGain

## Структура алгоритма
def chooseBestFeatureToSplitByID3(dataSet):
    """
         Выберите лучший раздел набора данных
    :param dataSet:
    :return:
    """
    numFeatures = len(dataSet[0]) -1 # Последний столбец категории
    baseEntropy = calcShannonEnt(dataSet) # Возврат информационной энтропии всего набора данных
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures): # Пройдите по всем элементам измерения
        infoGain = calcInformationGain(dataSet,baseEntropy,i) # Возвращение информации о наборе специфических функций
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature # Возвращает размер, соответствующий лучшему элементу

def createTree(dataSet,featureName,chooseBestFeatureToSplitFunc = chooseBestFeatureToSplitByID3):
    """
         Создать дерево решений
         : param dataSet: набор данных
         : param featureName: имя каждого измерения набора данных
         : return: дерево решений
    """
    classList = [example[-1] for example in dataSet] # Список категорий
    if classList.count(classList[0]) == len(classList): # Подсчитать количество classList [0]
        return classList[0] # Когда категории абсолютно совпадают, прекратите деление
    if len(dataSet[0]) ==1: # Когда есть только одна функция, переберите все экземпляры, чтобы получить наиболее частую категорию
        return majorityCnt(classList) # Вернуться к тегам категории
    bestFeat = chooseBestFeatureToSplitFunc(dataSet)# Лучший признак соответствующего индекса
    bestFeatLabel = featureName[bestFeat] # Лучшая особенность
    myTree ={bestFeatLabel:{}}  # структура и ключ карты - featureLabel
    del (featureName[bestFeat])
    # Найти подмножество функций для классификации
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = featureName[:] # Операция копирования
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree

# Тестирование построения дерева решений
dataSet,featureName = createDataSet()
myTree = createTree(dataSet,featureName)
print(myTree)