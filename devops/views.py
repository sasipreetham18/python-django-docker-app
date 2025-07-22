from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
            <head><title>DevOps by Preetham</title></head>
            <body style="font-family:sans-serif; text-align:center; margin-top:100px;">
                <h1>🚀 Hello, I'm Dasari Sasi Preetham</h1>
                <h2>👨‍💻 Aspiring DevOps Engineer</h2>
                <p>DOB: 18th October 2001</p>
                <p>Skilled in Docker, Jenkins, Git, Linux, and CI/CD automation.</p>
                <p>Building projects to deploy scalable apps with Docker + Django.</p>
                <hr>
                <p style="color:gray;">This page is running inside a Docker container 🐳</p>
            </body>
        </html>
    """)


