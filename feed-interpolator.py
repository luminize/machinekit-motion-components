#!/usr/bin/env python2
import os, time
import random

from   machinekit import hal
from   machinetalk.protobuf.ros_pb2 import *
import google.protobuf.text_format

name1 = "interpolator.1.traj"
name2 = "interpolator.2.traj"
name3 = "interpolator.3.traj"
r1 = hal.Ring(name1)
r2 = hal.Ring(name2)
r3 = hal.Ring(name3)
sign = 1
period = 0.5 # sec
step = 10
position = step
ts = 0
n=1

vmax_jplan = position / (0.5 * period)
amax_jplan = vmax_jplan / (0.5 * period)

tp = JointTrajectoryPoint()
tp.positions.append(10)
tp.velocities.append(0)
tp.accelerations.append(0)
ts += period

tp.time_from_start = ts
tp.serial = 1
buffer = tp.SerializeToString()
r1.write(buffer)
r2.write(buffer)
r3.write(buffer)
hal.Pin("jplanner.0.max-vel").set(vmax_jplan)
hal.Pin("jplanner.0.max-acc").set(amax_jplan)
hal.Pin("jplanner.0.pos-cmd").set(position)
    