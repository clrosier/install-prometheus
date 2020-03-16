pipeline {
    environment {
        // Environment here
    }

    agent any

    stages {
        stage ('Run molecule tests') {
            // The idea here is to run molecule tests on the user's changes to ensure
            // that nothing breaks
            steps {
                script {
                    sh "cd roles/install && molecule test"
                }
            }
        }

        stage ('Call playbook') {
            // After successful testing, call out to playbook to deploy changes
            steps {
                script {
                    sh "ansible-playbook -i $HOSTS_FILE $WORKSPACE/install-prometheus/main.yml"
                }
            }
        }
    }
}