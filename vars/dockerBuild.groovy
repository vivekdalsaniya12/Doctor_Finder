def call(String dockerimage, String imageversion, String path) {
    echo "Building Docker image: ${dockerimage}:${imageversion} from path ${path}"
    sh "docker build -t ${dockerimage}:${imageversion} ${path}"
}
