# 역량평가 파이썬 중급 2번 문제
""""
북에서 운영하는 새로운 홈페이지를 발견하여 
메인 페이지에 링크되어있는 관련 사이트를 파싱하고자 합니다. 
다양한 형태의 URL을 파싱하여 출력하세요.
"""
import re

str_list = """<!doctype html>
<html class="notion-html">
  <head lang="en">
    <meta name="twitter:url" content="https://www.notion.so">
    <meta name="twitter:image" content="https://www.notion.so/images/meta/default.png">
    <link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico">
    <link href="/app-6b6a1c97dc3362bbd58b.css" rel="stylesheet">
  </head>
  <body class="notion-body">
    <script>
      var parsed, theme = "light",
      !themeRecord || (parsed = JSON.parse(themeRecord)) && parsed.mode && (theme = parsed.mode), "dark" === theme && document.body.classList.add("dark")
    </script>
    <style>
      .notion-front-page #skeleton,
      .notion-mobile #skeleton {
        display: none
      }

      body.dark .startup-shimmer::before {
        background: linear-gradient(90deg, transparent 0, rgba(86, 86, 86, .4) 50%, transparent 100%)
      }

      #skeleton.isElectron .draggable {
        display: block
      }
    </style>
    <div id="initial-loading-spinner"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
        protocol: "notion",
        staticS3: {
          url: "https://prod-notion-assets.s3-us-west-2.amazonaws.com",
          bucket: "prod-notion-assets"
        },
        lastUpdatedTime: 1674691155038,
        api: {
          http: "/api/v3"
        },
        googleOAuth: {
          clientId: "905154081809-858sm3f0qnalqd9d44d9gecjtrdji9tf.apps.googleusercontent.com"
        },
        messageStore: {
          url: "https://msgstore.www.notion.so",
          api: "/api/v1"
        },
        secureFileConfig: {
          s3BaseDomainName: "s3.us-west-2.amazonaws.com",
          rootPath: "/f",
          protocol: "https",
          hostname: "file.notion.so"
        },

        iframely: {
          key: "222a85036317ca50d3ba5f321bfda6f0"
        },
        aif: {
          url: "https://aif.notion.so/aif-production.html"
        },
        statsig: {
          apiKey: "client-Tgza5wNFa8dVt9BdeUfG6Vkm29bHxX10MhoztTMzLBB"
        },
        google: {
          clientId: "905154081809-858sm3f0qnalqd9d44d9gecjtrdji9tf.apps.googleusercontent.com"
        },
        }
      }
    </script>
  </body>
</html>""".split('\n')
print(str_list)