import wpilib
from commands2 import TimedCommandRobot
from shooter import Shooter
from intake import Intake
from ledsubsystem import LEDSubsystem

from flywheelCommand import ControlFlywheel
from indexerCommand import ControlIndexer
from timedIndexer import TimedIndexer
from fireinthehole import FireInTheHole
from commands2.button import CommandXboxController
from update_speed_variable import Update_Speed_Variable
from enable_Flywheel import Enable_flywheel
from phoenix6.signal_logger import SignalLogger

class MyRobot(TimedCommandRobot):
   def robotInit(self):
       """
       This function is called upon program startup and
       should be used for any initialization code.
       """
       self._driver_controller = CommandXboxController(0)
       self._shooter: Shooter = Shooter()
       self._shooter.setDefaultCommand(ControlFlywheel(self._shooter,  0))

       self._intake: Intake = Intake()
       self._led:   LEDSubsystem = LEDSubsystem()
       

    #    SignalLogger.start()                 # Enable CTRE Motor Hoot logging.


    # Revised code to have a global variable controlling the speed
    # A boolean enables/disables the flywheel
    # The global speed is controlled by the POV buttons
    # Enable/Disable is controlled by the A and B button


       self._driver_controller.a().onTrue(Enable_flywheel(self._shooter, True))
       self._driver_controller.b().onTrue(Enable_flywheel(self._shooter, False))

       self._driver_controller.x().whileTrue(ControlIndexer(self._shooter, 0.2))
       self._driver_controller.y().whileTrue(ControlIndexer(self._shooter, 0) )
       self._driver_controller.rightTrigger().onTrue(TimedIndexer(self._shooter, 0.2, 1)       )
       self._driver_controller.leftTrigger().onTrue(FireInTheHole(self._shooter, 0.2, 5))


       self._driver_controller.povUp().onTrue(Update_Speed_Variable(self._shooter, 0.05))   # Increase the motor speed by 0.1
       self._driver_controller.povDown().onTrue(Update_Speed_Variable(self._shooter, -0.05))

       wpilib.DriverStation.silenceJoystickConnectionWarning(True)


       print ("Robot Initialization (robotInit) Completed ")


   def autonomousInit(self):
       """This function is run once each time the robot enters autonomous mode."""
       print ("Autonomous Initialization (autonomousInit) Completed ")


   def autonomousPeriodic(self):
       """This function is called periodically during autonomous."""


   def teleopInit(self):
       """This function is called once each time the robot enters teleoperated mode."""
       print ("TeleOpInit Initialization (teleopInit) Completed ")


   def teleopPeriodic(self):
       """This function is called periodically during teleoperated mode."""
       pass


   def testInit(self):
       """This function is called once each time the robot enters test mode."""
       print ("TestInit Initialization (testInit) Completed ")


   def testPeriodic(self):
       """This function is called periodically during test mode."""
