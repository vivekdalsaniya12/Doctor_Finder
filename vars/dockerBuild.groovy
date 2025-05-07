def call(String dockerimage, String imageversion){
  docker build -t dockerimage:imageversion .
}
