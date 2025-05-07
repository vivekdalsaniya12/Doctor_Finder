def call(String dockerimage, String imageversion, String path){
  sh "docker build -t ${dockerimage}:${imageversion} ${path}"
}
