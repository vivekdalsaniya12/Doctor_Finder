def call(String dockerimage, String imageversion, String path) {
    sh "pwd"
    sh "docker build -t ${dockerimage}:${imageversion} ${path}"
}
