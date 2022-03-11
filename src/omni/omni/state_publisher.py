import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from sensor_msgs.msg import JointState

class StatePublisher(Node):

    def __init__(self):
        rclpy.init()
        super().__init__('state_publisher')

        qos_profile = QoSProfile(depth=10)
        self.joint_pub = self.create_publisher(JointState, 'joint_states', qos_profile)
        self.nodeName = self.get_name()
        self.get_logger().info("{0} started".format(self.nodeName))

        loop_rate = self.create_rate(1000)

        # message declarations
        joint_state = JointState()
        joint_state.name = ['waist', 'shoulder', 'elbow', 'yaw', 'pitch', 'roll']
        joint_state.position = [0.0, 0.0, 0.0, 0.0, 0.1, 0.0]
        try:
            while rclpy.ok():
                rclpy.spin_once(self)

                # update joint_state
                now = self.get_clock().now()
                joint_state.header.stamp = now.to_msg()
                joint_state.position[0] += 0.001

                # send the joint state and transform
                self.joint_pub.publish(joint_state)

                # This will adjust as needed per iteration
                loop_rate.sleep()

        except KeyboardInterrupt:
            pass

def main():
    node = StatePublisher()

if __name__ == '__main__':
    main()
