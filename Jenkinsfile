pipeline {
    agent any

    environment {
        WORKDIR = "project_root"
        VENV = "venv"
    }

    stages {

        stage('준비') {
            steps {
                checkout scm
                echo "📌 HelpyChat QA Pipeline Started"

                dir("${WORKDIR}") {
                    echo "📁 working directory: ${WORKDIR}"
                }
            }
        }

        stage('의존성 설치') {
            steps {
                script {
                    dir("${WORKDIR}") {
                        if (isUnix()) {
                            sh """
                                python3 -m venv ../${VENV}
                                . ../${VENV}/bin/activate
                                pip install --upgrade pip
                                pip install -r requirements.txt
                            """
                        } else {
                            bat """
                                python -m venv ..\\${VENV}
                                call ..\\${VENV}\\Scripts\\activate
                                pip install --upgrade pip
                                pip install -r requirements.txt
                            """
                        }
                    }
                }
            }
        }

        stage('전체 테스트 실행') {
            steps {
                script {
                    dir("${WORKDIR}") {
                        if (isUnix()) {
                            sh """
                                . ../${VENV}/bin/activate
                                pytest tests -v \
                                    --junit-xml=../reports/all-results.xml \
                                    --html=../reports/report.html \
                                    --self-contained-html
                            """
                        } else {
                            bat """
                                call ..\\${VENV}\\Scripts\\activate
                                pytest tests -v ^ 
                                    --junit-xml=..\\reports\\all-results.xml ^ 
                                    --html=..\\reports\\report.html ^ 
                                    --self-contained-html
                            """
                        }
                    }
                }
            }
        }

        stage('커버리지 분석') {
            steps {
                script {
                    dir("${WORKDIR}") {
                        if (isUnix()) {
                            sh """
                                . ../${VENV}/bin/activate
                                pytest --cov=src \
                                       --cov-report=html:../reports/htmlcov \
                                       --cov-report=xml:../reports/coverage.xml
                            """
                        } else {
                            bat """
                                call ..\\${VENV}\\Scripts\\activate
                                pytest --cov=src ^
                                       --cov-report=html:..\\reports\\htmlcov ^
                                       --cov-report=xml:..\\reports\\coverage.xml
                            """
                        }
                    }
                }
            }
        }

        stage('배포') {
            when { anyOf { branch 'develop'; branch 'main' } }
            steps {
                echo "🚀 배포 단계 (여기서는 메시지만 출력)"
            }
        }
    }

    post {
        always {
            // JUnit 테스트 결과
            junit "reports/all-results.xml"

            // HTML 커버리지 보고서
            publishHTML([
                reportDir: 'reports/htmlcov',
                reportFiles: 'index.html',
                reportName: 'Coverage Report'
            ])

            // HTML 테스트 보고서
            publishHTML([
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Test HTML Report'
            ])
        }

        success {
            echo "✅ HelpyChat QA Pipeline ALL PASSED!"
        }

        failure {
            echo "❌ Pipeline FAILED — 확인 필요"
        }
    }
}
