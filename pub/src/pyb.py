#!/usr/bin/env python
from sensor_msgs.msg import Range
from sensor_msgs.msg import LaserScan
import rospy
import math

ranges = []
for i in range(0,8):
    ranges.append(0)
def publish():
    scan_pub = rospy.Publisher('scan', LaserScan, queue_size=50)  
    num_readings = 8
    laser_frequency = 240
    count = 0
    r = rospy.Rate(100)
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
        scan = LaserScan()
        scan.header.stamp = current_time
        scan.header.frame_id = 'ultra_Link'
        scan.angle_min = 0
        scan.angle_max = 2*math.pi
        scan.angle_increment = 2*3.14 / num_readings
        scan.time_increment = (1.0 / laser_frequency) / (num_readings)
        scan.range_min = 0.05
        scan.range_max = 10
        scan.ranges = ranges
        scan.intensities = []
        for i in range(0, num_readings):
            scan.intensities.append(0)  
            
        scan_pub.publish(scan)
        count += 1  
        r.sleep()

def callback(Range):
    
    for i in range(0,len(ranges)+1):
        stri = str(i)
        link_num = "ultra" + stri + "_link"
        if Range.header.frame_id == link_num :
            ranges[i-1] = Range.range       
def listener():
    rospy.init_node('pub', anonymous=False)
    rospy.Subscriber("/sensor/ir_1", Range, callback)
    rospy.Subscriber("/sensor/ir_2", Range, callback)
    rospy.Subscriber("/sensor/ir_3", Range, callback)
    rospy.Subscriber("/sensor/ir_4", Range, callback)
    rospy.Subscriber("/sensor/ir_5", Range, callback)
    rospy.Subscriber("/sensor/ir_6", Range, callback)
    rospy.Subscriber("/sensor/ir_7", Range, callback)
    rospy.Subscriber("/sensor/ir_8", Range, callback)    
    publish()
    rospy.spin()

if __name__ == '__main__':
    listener()