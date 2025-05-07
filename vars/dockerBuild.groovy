def call(Map x){
  sh 'docker build -t x.docker_image:x.image_tag x.path'
}
