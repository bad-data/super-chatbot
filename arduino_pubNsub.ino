
#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle nh;

void messageCb(const std_msgs::String& command) {
   x = command.data;
   if (x == '0') {
    digitalWrite(13,LOW);
   } 
   else if(x == '1') {
     digitalWrite(13,HIGH);
   }
}

std_msgs::String str_msg;
ros::Subscriber<std_msgs::String> messageSub('subscriber', &messageCb);
ros::Publisher dataPub('publisher', &str_msg);

void setup() {
  nh.initNode();
  nh.subscribe(messageSub);
  nh.advertise(dataPub);
}

void loop() {
  str_msg.data = "data recieved";
  dataPub.publish(&str_msg);
  nh.spinOnce();
  delay(100);
}
