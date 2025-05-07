def call(Map x){
  // sh 'docker build -t ${x.dockerimage}:${x.imagetag} ${x.path}'
  echo "hello worldddd"
  sh 'echo "inside sh command"'
  sh 'docker build -t vivekdalsaniya/doctor_finder:latest .'
}
