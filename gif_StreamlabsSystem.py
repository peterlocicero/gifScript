import sys
import json
import os
import ctypes
import codecs
import time

ScriptName = "Gif"
Website = "Twitch.tv/nebulicianbot"
Description = "Runs a gif on stream"
Creator = "Dameyen"
Version = "1.0.0"
Command = '!gif'


configFile = "config.json"
settings = {}
emotes = []
responses = []

def Init():
    global settings

    path = os.path.dirname(__file__)
    try:
        with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
            settings = json.load(file, encoding='utf-8-sig')
    except:
        print('Could not open file.log')

    
    return




def Execute(data):
    
    
    if data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        userId = data.User			
        username = data.UserName
        points = Parent.GetPoints(userId)
        command = "Squidward"
        commandNum = ""
        gifs(userId,username,points,command,commandNum)
        return
    
    elif data.IsChatMessage() and data.GetParam(0).lower() == settings["command2"] and Parent.HasPermission(data.User, settings["permission2"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        userId = data.User			
        username = data.UserName
        points = Parent.GetPoints(userId)
        command = "Dancing for Jesus"
        commandNum = "2"
        gifs(userId,username,points,command,commandNum)
        return
    elif data.IsChatMessage() and data.GetParam(0).lower() == settings["command3"] and Parent.HasPermission(data.User, settings["permission3"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        userId = data.User			
        username = data.UserName
        points = Parent.GetPoints(userId)
        command = "Dive"
        commandNum = "3"
        gifs(userId,username,points,command,commandNum)
        return
    elif data.IsChatMessage() and data.GetParam(0).lower() == settings["command4"] and Parent.HasPermission(data.User, settings["permission4"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        userId = data.User			
        username = data.UserName
        points = Parent.GetPoints(userId)
        command = "Fortnite"
        commandNum = "4"
        gifs(userId,username,points,command,commandNum)
        return
    elif data.IsChatMessage() and data.GetParam(0).lower() == settings["command5"] and Parent.HasPermission(data.User, settings["permission5"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        userId = data.User			
        username = data.UserName
        points = Parent.GetPoints(userId)
        command = "Internet Man"
        commandNum = "5"
        gifs(userId,username,points,command,commandNum)
        return
    elif data.IsChatMessage() and data.GetParam(0).lower() == settings["command6"] and Parent.HasPermission(data.User, settings["permission6"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        userId = data.User			
        username = data.UserName
        points = Parent.GetPoints(userId)
        command = "Thanos"
        commandNum="6"
        gifs(userId,username,points,command,commandNum)
        return
    return

def gifs(userId, username, points,command,commandNum):
        costed="costs"+commandNum
        useCooldown="useCooldown"+commandNum
        commands="command"+commandNum
        setTime="setTime"+commandNum
        coolDown ="Cooldown"+commandNum

        
        costs=settings[costed]
    
        if (costs > points or costs < 1):
            currency = Parent.GetCurrencyName()
            sendMessage(username + " you do not have enough " + currency + "!")
        elif settings[useCooldown] and (Parent.IsOnCooldown(ScriptName, settings[commands]) or Parent.IsOnUserCooldown(ScriptName,settings[commands], userId)):
            sendMessage(username + " this command is on cooldown!")
            
        else:
            sendMessage(username + " Gif activated!")
            Parent.RemovePoints(userId, username, costs)
            duration = int(settings[setTime])
            Parent.SetOBSSourceRender(command, True, "LIVE",callback)
            time.sleep(duration)
            Parent.SetOBSSourceRender(command, False, "LIVE",callback)
            if settings[useCooldown]:
                Parent.AddCooldown(ScriptName, settings[commands], settings[coolDown])
        return


def callback(jsonString):
    Parent.log(Command,jsonString);
    return


def sendMessage(message):
    Parent.SendStreamMessage(message)
    return

def log(message):
    Parent.Log(Command,message)
    return


def Tick():
    return





