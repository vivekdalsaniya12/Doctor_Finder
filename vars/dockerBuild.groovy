def call(String dockerimage, String imageversion, String path){
  docker build -t dockerimage:imageversion path
}
