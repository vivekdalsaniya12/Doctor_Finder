def call(Map x){
  sh """
      echo ${x.PASSWORD} | docker login -u ${x.USERNAME} --password-stdin
      docker push ${x.DOCKER_IMAGE}:${x.IMAGE_TAG}
      docker logout
  """
}
