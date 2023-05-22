#!/usr/bin/env python
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatusArray
import ui1
import rospy
from nav_msgs.msg import Odometry

class MainWindow(QtWidgets.QMainWindow, ui1.Ui_MainWindow):
  
    def __init__(self):
        super().__init__()
        
        self.setupUi(self) 
        self.substatus = rospy.Subscriber("/move_base/status", GoalStatusArray, self.callbackStatus)
        self.odomstatus = rospy.Subscriber('/odom', Odometry, self.xycallback)
        self.Button1.clicked.connect(self.printPos1)
        self.Button2.clicked.connect(self.printPos2)
        self.Button3.clicked.connect(self.printPos3)
        self.Button4.clicked.connect(self.printPos4)
        self.Button5.clicked.connect(self.printPos5)
        self.Button6.clicked.connect(self.printPos6)
        self.Button7.clicked.connect(self.printPos7)
        self.Button8.clicked.connect(self.printPos8)
        self.Button9.clicked.connect(self.printPos9)
        self.Button10.clicked.connect(self.printPos10)
        self.Button11.clicked.connect(self.printPos11)
        self.Button12.clicked.connect(self.printPos12)
        self.Button13.clicked.connect(self.printPos13)
        self.Button14.clicked.connect(self.printPos14)
        self.Button15.clicked.connect(self.printPos15)
        self.Button16.clicked.connect(self.printPos16)
   
    def printPos1(self):
        x = self.Button1.property('CoordX')
        y = self.Button1.property('CoordY')
        w = self.Button1.property('CoordW')
        z = self.Button1.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos2(self):
        x = self.Button2.property('CoordX')
        y = self.Button2.property('CoordY')
        w = self.Button2.property('CoordW')
        z = self.Button2.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos3(self):
        x = self.Button3.property('CoordX')
        y = self.Button3.property('CoordY')
        w = self.Button3.property('CoordW')
        z = self.Button3.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos4(self):
        x = self.Button4.property('CoordX')
        y = self.Button4.property('CoordY')
        w = self.Button4.property('CoordW')
        z = self.Button4.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos5(self):
        x = self.Button5.property('CoordX')
        y = self.Button5.property('CoordY')
        w = self.Button5.property('CoordW')
        z = self.Button5.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos6(self):
        x = self.Button6.property('CoordX')
        y = self.Button6.property('CoordY')
        w = self.Button6.property('CoordW')
        z = self.Button6.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos7(self):
        x = self.Button7.property('CoordX')
        y = self.Button7.property('CoordY')
        w = self.Button7.property('CoordW')
        z = self.Button7.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos8(self):
        x = self.Button8.property('CoordX')
        y = self.Button8.property('CoordY')
        w = self.Button8.property('CoordW')
        z = self.Button8.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos9(self):
        x = self.Button9.property('CoordX')
        y = self.Button9.property('CoordY')
        w = self.Button9.property('CoordW')
        z = self.Button9.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos10(self):
        x = self.Button10.property('CoordX')
        y = self.Button10.property('CoordY')
        w = self.Button10.property('CoordW')
        z = self.Button10.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos11(self):
        x = self.Button11.property('CoordX')
        y = self.Button11.property('CoordY')
        w = self.Button11.property('CoordW')
        z = self.Button11.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos12(self):
        x = self.Button12.property('CoordX')
        y = self.Button12.property('CoordY')
        w = self.Button12.property('CoordW')
        z = self.Button12.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos13(self):
        x = self.Button13.property('CoordX')
        y = self.Button13.property('CoordY')
        w = self.Button13.property('CoordW')
        z = self.Button13.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos14(self):
        x = self.Button14.property('CoordX')
        y = self.Button14.property('CoordY')
        w = self.Button14.property('CoordW')
        z = self.Button14.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos15(self):
        x = self.Button15.property('CoordX')
        y = self.Button15.property('CoordY')
        w = self.Button15.property('CoordW')
        z = self.Button15.property('CoordZ')
        movebase_client(x,y,w,z)
    def printPos16(self):
        x = self.Button16.property('CoordX')
        y = self.Button16.property('CoordY')
        w = self.Button16.property('CoordW')
        z = self.Button16.property('CoordZ')
        movebase_client(x,y,w,z)

    def xycallback(self,data):
        self.label_5.setText(str(round(data.pose.pose.position.x,2)))
        self.label_6.setText(str(round(data.pose.pose.position.y,2)))
        

    def callbackStatus(self,data):
        if data.status_list[0].status == 4:
            self.label.setText('Failed to find a valid plan')
        elif data.status_list[0].status == 1:
            self.label.setText('moving to Goal')
        elif data.status_list[0].status == 3:
            self.label.setText('Goal reached')
        
        print(data.status_list[0].status)


def movebase_client(x,y,w,z):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    x1 = float(x)
    y1 = float(y)
    w1 = float(w)
    z1 = float(z)
    goal.target_pose.pose.position.x = x1
    goal.target_pose.pose.position.y = y1
    goal.target_pose.pose.orientation.w = w1
    goal.target_pose.pose.orientation.z = z1
    client.send_goal(goal)


def main():
    
    app = QtWidgets.QApplication(sys.argv)  
    window = MainWindow()
    window.show()  
    app.exec_()  



if __name__ == '__main__':  

    rospy.init_node('new_goal_publisher')
    
    main()  