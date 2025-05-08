withCredentials ([usernamePassword(credentialsId:'dockercreds',usernameVariable:'USERNAME',passwordVariable:'PASSWORD')]) 
{
  sh '''
      echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
      docker push $DOCKER_IMAGE:$IMAGE_TAG
      docker logout
  '''
}
