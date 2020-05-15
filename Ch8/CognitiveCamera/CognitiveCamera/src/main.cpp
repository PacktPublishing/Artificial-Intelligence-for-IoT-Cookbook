#include "WiFi.h"
#include "esp_camera.h"
//#include "esp_timer.h"
//#include "img_converters.h"

//#include "soc/soc.h"           // Disable brownour problems
//#include "soc/rtc_cntl_reg.h"  // Disable brownour problems
//#include "driver/rtc_io.h"
//#include <StringArray.h>
//#include <SPIFFS.h>
//#include <FS.h>


// Replace with your network credentials
const char* ssid = "";
const char* password = "";


// Photo File Name to save in SPIFFS
#define FILE_PHOTO "/photo.jpg"

// OV2640 camera module pins (CAMERA_MODEL_AI_THINKER)
#define PWDN_GPIO_NUM    -1
#define RESET_GPIO_NUM   -1
#define XCLK_GPIO_NUM    4
#define SIOD_GPIO_NUM    18
#define SIOC_GPIO_NUM    23
#define Y9_GPIO_NUM      36
#define Y8_GPIO_NUM      37
#define Y7_GPIO_NUM      38
#define Y6_GPIO_NUM      39
#define Y5_GPIO_NUM      35
#define Y4_GPIO_NUM      14
#define Y3_GPIO_NUM      13
#define Y2_GPIO_NUM      34
#define VSYNC_GPIO_NUM   5
#define HREF_GPIO_NUM    27
#define PCLK_GPIO_NUM    25


void setup() {
  // Serial port for debugging purposes
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(5000);
 
 Serial.println(WiFi.status());
  WiFi.begin(ssid, password);
   delay(500);
  
    Serial.println("Connecting to WiFi...");
  
  }
/*
  if (!SPIFFS.begin(true)) {
    Serial.println("An Error has occurred while mounting SPIFFS");
  //  ESP.restart();
  }
  else {
    delay(500);
    Serial.println("SPIFFS mounted successfully");
  }
*/
  // Print ESP32 Local IP Address
  Serial.print("IP Address: http://");
  Serial.println(WiFi.localIP());

  // Turn-off the 'brownout detector'
  //WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0);


/*
  // OV2640 camera module
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;

  if (psramFound()) {
    config.frame_size = FRAMESIZE_UXGA;
    config.jpeg_quality = 10;
    config.fb_count = 2;
  } else {
    config.frame_size = FRAMESIZE_SVGA;
    config.jpeg_quality = 12;
    config.fb_count = 1;
  }
  // Camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    //ESP.restart();
  }



*/
}


/*
// Check if photo capture was successful
bool checkPhoto( fs::FS &fs ) {
  File f_pic = fs.open( FILE_PHOTO );
  unsigned int pic_sz = f_pic.size();
  return ( pic_sz > 100 );
}
/*
// Capture Photo and Save it to SPIFFS
void capturePhotoSaveSpiffs( void ) {
  camera_fb_t * fb = NULL; // pointer
  bool ok = 0; // Boolean indicating if the picture has been taken correctly

  do {
    // Take a photo with the camera
    Serial.println("Taking a photo...");

    fb = esp_camera_fb_get();
    if (!fb) {
      Serial.println("Camera capture failed");
      return;
    }

    // Photo file name
  
/*
    Serial.printf("Picture file name: %s\n", FILE_PHOTO);
    File file = SPIFFS.open(FILE_PHOTO, FILE_WRITE);

    // Insert the data in the photo file
    if (!file) {
      Serial.println("Failed to open file in writing mode");
    }
    else {
      file.write(fb->buf, fb->len); // payload (image), payload length
      Serial.print("The picture has been saved in ");
      Serial.print(FILE_PHOTO);
      Serial.print(" - Size: ");
      Serial.print(file.size());
      Serial.println(" bytes");
    }
    // Close the file
    file.close();
    esp_camera_fb_return(fb);

    // check if file has been correctly saved in SPIFFS
    ok = checkPhoto(SPIFFS);
  } while ( !ok );
}
*/
/*
void sendPhoto(void)
{
File file = SPIFFS.open(FILE_PHOTO, FILE_READ);

String start_request = ""; String end_request = "";

//headers = {'Prediction-Key': '9c5da3f162c04c45b85be1eb5c2ca33b', 'Content-Type':'application/octet-stream'}

start_request = start_request +
                "\n--AaB03x\n" +
                "\nPrediction-Key: 9c5da3f162c04c45b85be1eb5c2ca33b\n" +
                "\nContent-Type: application/octet-stream\n\n";
end_request = end_request + "\n--AaB03x--\n";
uint16_t full_length;

full_length = start_request.length() + file.size() + end_request.length();

WiFiClient client;
if (!client.connect("https://aibenchtest.cognitiveservices.azure.com/customvision/v3.0/Prediction/6ea65006-0a20-4518-b916-7eca7f1f197e/detect/iterations/Iteration1/image", 80)) {
  Serial.println("Connected FILED!");
  return;
}

/*

url = 'https://aibenchtest.cognitiveservices.azure.com/customvision/v3.0/Prediction/6ea65006-0a20-4518-b916-7eca7f1f197e/detect/iterations/Iteration1/image'
#payload = {'client_id': 1}
files = {'file': file}
r = requests.post(url,  data=file, headers=headers)
json_data = r.json()

*/
/*

Serial.println("Connected ok!");
client.println("POST /Home/Index HTTP/1.1");
client.println("Host: example.com");
client.println("User-Agent: ESP32");
client.println("Content-Type: application/octet-stream");
client.print("Content-Length: "); 
client.println(full_length);
client.println();
client.print(start_request);

while (file.available()){
  client.write(file.read());
}

Serial.println(">>><<<");
client.println(end_request);

}
*/
void loop() {

//    capturePhotoSaveSpiffs();
  
  delay(10000);

  Serial.println("loop");

  // put your main code here, to run repeatedly:

/*

file = open('images/drink1/cap0.jpg', 'rb')
url = 'https://aibenchtest.cognitiveservices.azure.com/customvision/v3.0/Prediction/6ea65006-0a20-4518-b916-7eca7f1f197e/detect/iterations/Iteration1/image'
headers = {'Prediction-Key': '9c5da3f162c04c45b85be1eb5c2ca33b', 'Content-Type':'application/octet-stream'}
#payload = {'client_id': 1}
files = {'file': file}
r = requests.post(url,  data=file, headers=headers)
json_data = r.json()

*/


}