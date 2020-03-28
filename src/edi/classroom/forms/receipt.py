# -*- coding: utf-8 -*-
from datetime import datetime

def create_userbody(data):
    body = u"""\
<!doctype html>
<html>
  <head>
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Receipt</title>
    <style media="all" type="text/css">
    /* -------------------------------------
    GLOBAL RESETS
------------------------------------- */
    
    img {
      border: none;
      -ms-interpolation-mode: bicubic;
      max-width: 100%;
    }
    
    .img-block {
      display: block;
    }
    
    body {
      font-family: Helvetica, sans-serif;
      -webkit-font-smoothing: antialiased;
      font-size: 14px;
      line-height: 1.4;
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
    }
    
    table {
      border-collapse: separate;
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
      width: 100%;
    }
    
    table td {
      font-family: Helvetica, sans-serif;
      font-size: 14px;
      vertical-align: top;
    }
    /* -------------------------------------
    BODY & CONTAINER
------------------------------------- */
    
    body {
      background-color: #f6f6f6;
      margin: 0;
      padding: 0;
    }
    
    .body {
      background-color: #f6f6f6;
      width: 100%;
    }
    
    .container {
      margin: 0 auto !important;
      max-width: 600px;
      padding: 0;
      padding-top: 24px;
      width: 600px;
    }
    
    .content {
      box-sizing: border-box;
      display: block;
      margin: 0 auto;
      max-width: 600px;
      padding: 0;
    }
    /* -------------------------------------
    HEADER, FOOTER, MAIN
------------------------------------- */
    
    .main {
      background: #fff;
      border-radius: 4px;
      width: 100%;
    }
    
    .wrapper {
      box-sizing: border-box;
      padding: 24px;
    }
    
    .content-block {
      padding-top: 0;
      padding-bottom: 24px;
    }
    
    .flush-top {
      margin-top: 0;
      padding-top: 0;
    }
    
    .flush-bottom {
      margin-bottom: 0;
      padding-bottom: 0;
    }
    
    .header {
      margin-bottom: 24px;
      margin-top: 0;
      width: 100%;
    }
    
    .header > table {
      min-width: 100%;
    }
    
    .footer {
      clear: both;
      padding-top: 24px;
      text-align: center;
      width: 100%;
    }
    
    .footer td,
    .footer p,
    .footer span,
    .footer a {
      color: #999999;
      font-size: 12px;
      text-align: center;
    }
    /* -------------------------------------
    HIGHLIGHT SECTION
------------------------------------- */
    
    .section-callout {
      background-color: #1abc9c;
      color: #ffffff;
    }
    
    .section-callout h1,
    .section-callout h2,
    .section-callout h3,
    .section-callout h4,
    .section-callout p,
    .section-callout li,
    .section-callout td {
      color: #ffffff;
    }
    
    .section-callout-subtle {
      background-color: #f7f7f7;
      border-bottom: 1px solid #e9e9e9;
      border-top: 1px solid #e9e9e9;
    }
    /* -------------------------------------
    GRID
    Assume the grid is a 6 column grid (spanning 6 columns).
    Therefore if you want 2 columns, each 50% in width, those columns would be span-3.
    Note that due to inline-block these elements must start/stop beside each other.
    i.e. no line breaks or spaces
------------------------------------- */
    
    .span-2,
    .span-3 {
      display: inline-block;
      margin-bottom: 24px;
      vertical-align: top;
      width: 100%;
    }
    
    .span-2 > table,
    .span-3 > table {
      padding-left: 24px;
      padding-right: 24px;
    }
    
    .span-3 {
      max-width: 298px;
    }
    
    .span-3 > table {
      max-width: 298px;
    }
    
    .span-2 {
      max-width: 197px;
    }
    
    .span-2 > table {
      max-width: 197px;
    }
    /* -------------------------------------
    RESPONSIVE AND MOBILE FRIENDLY STYLES
------------------------------------- */
    
    @media only screen and (max-width: 640px) {
      .span-2,
      .span-3 {
        float: none !important;
        max-width: none !important;
        width: 100% !important;
      }
      .span-2 > table,
      .span-3 > table {
        max-width: 100% !important;
        width: 100% !important;
      }
    }
    /* -------------------------------------
    TYPOGRAPHY
------------------------------------- */
    
    h1,
    h2,
    h3,
    h4 {
      color: #222222;
      font-family: Helvetica, sans-serif;
      font-weight: 400;
      line-height: 1.4;
      margin: 0;
    }
    
    h1 {
      font-size: 36px;
      font-weight: 300;
      margin-bottom: 24px;
      text-align: center;
      text-transform:none;
    }
    
    h2 {
      font-size: 28px;
      margin-bottom: 16px;
    }
    
    h3 {
      font-size: 22px;
      margin-bottom: 8px;
    }
    
    h4 {
      font-size: 14px;
      font-weight: 500;
      margin-bottom: 8px;
    }
    
    p,
    ul,
    ol {
      font-family: Helvetica, sans-serif;
      font-size: 14px;
      font-weight: normal;
      margin: 0;
      margin-bottom: 16px;
    }
    
    p li,
    ul li,
    ol li {
      list-style-position: outside;
      margin-left: 16px;
      padding: 0;
      text-indent: 0;
    }
    
    ul,
    ol {
      margin-left: 8px;
      padding: 0;
      text-indent: 0;
    }
    
    a {
      color: #3498db;
      text-decoration: underline;
    }
    /* -------------------------------------
    BUTTONS
------------------------------------- */
    
    .btn {
      box-sizing: border-box;
      min-width: 100% !important;
      width: 100%;
    }
    
    .btn > tbody > tr > td {
      padding-bottom: 16px;
    }
    
    .btn table {
      width: auto;
    }
    
    .btn table td {
      background-color: #ffffff;
      border-radius: 4px;
      text-align: center;
    }
    
    .btn a {
      background-color: #ffffff;
      border: solid 2px #3498db;
      border-radius: 4px;
      box-sizing: border-box;
      color: #3498db;
      cursor: pointer;
      display: inline-block;
      font-size: 14px;
      font-weight: bold;
      margin: 0;
      padding: 12px 24px;
      text-decoration: none;
      text-transform: capitalize;
    }
    
    .btn-primary table td {
      background-color: #3498db;
    }
    
    .btn-primary a {
      background-color: #3498db;
      border-color: #3498db;
      color: #ffffff;
    }
    
    @media all {
      .btn-primary table td:hover {
        background-color: #34495e !important;
      }
      .btn-primary a:hover {
        background-color: #34495e !important;
        border-color: #34495e !important;
      }
    }
    
    .btn-secondary table td {
      background-color: transparent;
    }
    
    .btn-secondary a {
      background-color: transparent;
      border-color: #3498db;
      color: #3498db;
    }
    
    @media all {
      .btn-secondary a:hover {
        border-color: #34495e !important;
        color: #34495e !important;
      }
    }
    
    .btn-tertiary table td {
      background-color: transparent;
    }
    
    .btn-tertiary a {
      background-color: transparent;
      border-color: #ffffff;
      color: #ffffff;
    }
    /* -------------------------------------
    ALERTS
------------------------------------- */
    
    .alert {
      min-width: 100%;
    }
    
    .alert td {
      border-radius: 4px 4px 0 0;
      color: #ffffff;
      font-size: 14px;
      font-weight: 400;
      padding: 24px;
      text-align: center;
    }
    
    .alert a {
      color: #ffffff;
      font-size: 14px;
      font-weight: 400;
      text-decoration: none;
    }
    
    .alert.alert-warning td {
      background-color: #f39c12;
    }
    
    .alert.alert-danger td {
      background-color: #c0392b;
    }
    
    .alert.alert-success td {
      background-color: #1abc9c;
    }
    /* -------------------------------------
    RECEIPT
------------------------------------- */
    
    .receipt {
      margin-bottom: 24px;
      width: 100%;
    }
    
    .receipt td {
      border-bottom: 1px solid #eee;
      margin: 0;
      padding: 8px;
    }
    
    .receipt td.receipt-figure {
      text-align: right;
    }
    
    .receipt .receipt-subtle {
      color: #aaa;
    }
    
    .receipt .receipt-bold td {
      border-bottom: 2px solid #333;
      border-top: 2px solid #333;
      font-size: 18px;
      font-weight: 600;
    }
    
    .receipt-container {
      width: 80%;
    }
    /* -------------------------------------
    ARTICLES
------------------------------------- */
    
    .article .article-thumbnail {
      padding-bottom: 8px;
    }
    
    .article .article-title {
      font-size: 14px;
      font-weight: 800;
      line-height: 1.4em;
      padding-bottom: 8px;
    }
    
    .article .article-title a {
      color: #222222;
      font-size: 14px;
      font-weight: 800;
      line-height: 1.4em;
      text-decoration: none;
    }
    
    .article .article-title .text-link {
      font-size: 22px;
    }
    
    .article .article-content {
      font-weight: normal;
      padding-bottom: 8px;
    }
    
    .article .article-meta {
      color: #999999;
      font-size: 12px;
    }
    
    .article .article-meta a {
      color: #999999;
    }
    
    .article .article-price {
      color: #9b59b6;
      font-size: 21px;
      font-weight: 600;
      padding-bottom: 8px;
    }
    
    .article .article-price-before {
      color: #c0392b;
      font-size: 14px;
      font-weight: 400;
      text-decoration: line-through;
    }
    /* -------------------------------------
    SOCIAL SHARING
------------------------------------- */
    
    .social-sharing {
      margin: 0 auto;
      text-align: center;
      width: auto;
    }
    
    .social-sharing-icon {
      height: 44px;
      margin: 0 2px;
    }
    
    .social-sharing-url {
      width: 100%;
    }
    
    .social-sharing-url td {
      background: rgba(255, 255, 255, 0.2);
      border: 2px dashed #ffffff;
      color: #ffffff;
      font-size: 18px;
      font-weight: 600;
      padding: 8px;
      text-align: center;
      vertical-align: middle;
    }
    
    .social-sharing-url-container {
      padding-bottom: 16px;
      padding-top: 0;
      width: 300px;
    }
    /* -------------------------------------
    OTHER STYLES THAT MIGHT BE USEFUL
------------------------------------- */
    
    .last {
      margin-bottom: 0;
    }
    
    .first {
      margin-top: 0;
    }
    
    .align-center {
      text-align: center;
    }
    
    .align-right {
      text-align: right;
    }
    
    .align-left {
      text-align: left;
    }
    
    .text-link {
      color: #3498db !important;
      text-decoration: underline !important;
    }
    
    .clear {
      clear: both;
    }
    
    .mt0 {
      margin-top: 0;
    }
    
    .mb0 {
      margin-bottom: 0;
    }
    
    .preheader {
      color: transparent;
      display: none;
      height: 0;
      max-height: 0;
      max-width: 0;
      opacity: 0;
      overflow: hidden;
      mso-hide: all;
      visibility: hidden;
      width: 0;
    }
    
    .powered-by a {
      text-decoration: none;
    }
    
    .hr tr:first-of-type td,
    .hr tr:last-of-type td {
      height: 24px;
      line-height: 24px;
    }
    
    .hr tr:nth-of-type(2) td {
      background-color: #f6f6f6;
      height: 1px;
      line-height: 1px;
      width: 100%;
    }
    /* -------------------------------------
    RESPONSIVE AND MOBILE FRIENDLY STYLES
------------------------------------- */
    
    @media only screen and (max-width: 640px) {
      h1 {
        font-size: 36px !important;
        margin-bottom: 16px !important;
      }
      h2 {
        font-size: 28px !important;
        margin-bottom: 8px !important;
      }
      h3 {
        font-size: 22px !important;
        margin-bottom: 8px !important;
      }
      .main p,
      .main ul,
      .main ol,
      .main td,
      .main span {
        font-size: 16px !important;
      }
      .wrapper {
        padding: 8px !important;
      }
      .article {
        padding-left: 8px !important;
        padding-right: 8px !important;
      }
      .content {
        padding: 0 !important;
      }
      .container {
        padding: 0 !important;
        padding-top: 8px !important;
        width: 100% !important;
      }
      .header {
        margin-bottom: 8px !important;
        margin-top: 0 !important;
      }
      .main {
        border-left-width: 0 !important;
        border-radius: 0 !important;
        border-right-width: 0 !important;
      }
      .btn table {
        max-width: 100% !important;
        width: 100% !important;
      }
      .btn a {
        font-size: 16px !important;
        max-width: 100% !important;
        width: 100% !important;
      }
      .img-responsive {
        height: auto !important;
        max-width: 100% !important;
        width: auto !important;
      }
      .alert td {
        border-radius: 0 !important;
        font-size: 16px !important;
        padding-bottom: 16px !important;
        padding-left: 8px !important;
        padding-right: 8px !important;
        padding-top: 16px !important;
      }
      .receipt,
      .receipt-container {
        width: 100% !important;
      }
      .hr tr:first-of-type td,
      .hr tr:last-of-type td {
        height: 16px !important;
        line-height: 16px !important;
      }
    }
    /* -------------------------------------
    PRESERVE THESE STYLES IN THE HEAD
------------------------------------- */
    
    @media all {
      .ExternalClass {
        width: 100%;
      }
      .ExternalClass,
      .ExternalClass p,
      .ExternalClass span,
      .ExternalClass font,
      .ExternalClass td,
      .ExternalClass div {
        line-height: 100%;
      }
      .apple-link a {
        color: inherit !important;
        font-family: inherit !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        text-decoration: none !important;
      }
    }
    </style>

    <!--[if gte mso 9]>
    <xml>
 <o:OfficeDocumentSettings>
  <o:AllowPNG/>
  <o:PixelsPerInch>96</o:PixelsPerInch>
 </o:OfficeDocumentSettings>
</xml>
<![endif]-->
  </head>
  <body>
    <table border="0" cellpadding="0" cellspacing="0" class="body">
      <tr>
        <td>&nbsp;</td>
        <td class="container">
          <div class="content">

            <!-- START CENTERED WHITE CONTAINER -->
            <span class="preheader">Vielen Dank für Ihre Bestellung auf kraeks.de</span>

            <!-- START HEADER -->
            <div class="header">
              <table border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td class="align-center">
                    <a href="https://educorvi.de" target="_blank"><img src="https://www.educorvi.de/@@site-logo/educorvi_logo.png" width="140" height="auto" alt="Logo der educorvi GmbH & Co. KG" align="center"></a>
                  </td>
                </tr>
              </table>
            </div>

            <!-- END HEADER -->
            <table border="0" cellpadding="0" cellspacing="0" class="main">

              <!-- START MAIN CONTENT AREA -->
              <tr>
                <td class="wrapper">
                  <table border="0" cellpadding="0" cellspacing="0">
                    <tr>
                      <td>
                        <h1>Ihre Bestellung auf kraeks.de</h1>
                        <h2 class="align-center">Ihre Rechnung</h2>
                        <table border="0" cellpadding="0" cellspacing="0">
                          <tr>
                            <td>&nbsp;</td>
                            <td class="receipt-container">
                              <table class="receipt" border="0" cellpadding="0" cellspacing="0">
                                <tr class="receipt-subtle">
                                  <td colspan="2" class="align-center">edi_form_date</td>
                                </tr>
                                <tr>
                                  <td>Handystativ 3D-Druck</td>
                                  <td class="receipt-figure">7,56</td>
                                </tr>
                                <tr>
                                  <td>Montage des Stativs</td>
                                  <td class="receipt-figure">inkl.</td>
                                </tr>
                                <tr>
                                  <td>Versand</td>
                                  <td class="receipt-figure">inkl.</td>
                                </tr>
                                <tr class="receipt-subtle">
                                  <td>Summe (netto)</td>
                                  <td class="receipt-figure">7,56</td>
                                </tr>
                                <tr class="receipt-subtle">
                                  <td>Mehrwertsteuer (19%)</td>
                                  <td class="receipt-figure">1,44</td>
                                </tr>
                                <tr class="receipt-bold">
                                  <td>Summe (brutto)</td>
                                  <td class="receipt-figure">9,00 €</td>
                                </tr>
                              </table>
                              <h2 class="align-center">Versand und Zahlung</h2>
                              <table class="receipt" border="0" cellpadding="0" cellspacing="0">
                                <tr>
                                  <td>Versand an:</td>
                                  <td>edi_form_name
                                    <br>edi_form_strhnr
                                    <br>edi_form_plz  edi_form_ort</td>
                                </tr>
                                <tr>
                                  <td>Zahlung an:</td>
                                  <td>educorvi GmbH & Co. KG
                                    <br>Steuer-Nummer: 218/157/05901
                                    <br>IBAN: DE96 7606 9372 0000 086010
                                    <br>BIC: GENODEF 1WDS
                                    <br>Verwendungszweck: 
                                    <br>Handystativ edi_form_mail</td>
                                </tr>
                              </table>
                              <p>Haben Sie Probleme? <a href="https://www.educorvi.de/kontakt" target="_blank">Kontaktieren Sie uns</a> und wir helfen Ihnen gern.</p>
                            </td>
                            <td>&nbsp;</td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>

              <!-- END MAIN CONTENT AREA -->
              </table>

            <!-- START FOOTER -->
            <div class="footer">
              <table border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td class="content-block">
                    <span class="apple-link">educorvi Gmbh & Co. KG, Karolinenstraße 17, 90763 Fürth</span>
                    <br><a href="https://educorvi.de">educorvi Homepage</a>
                    <br><a href="https://kraeks.de">kraeks.de Das Bildungsportal</a>
                  </td>
                </tr>
                <tr>
                  <td class="content-block powered-by">
                    Mail an uns: <a href="mailto: info@educorvi.de">info@educorvi.de</a>
                  </td>
                </tr>
              </table>
            </div>

            <!-- END FOOTER -->
            
<!-- END CENTERED WHITE CONTAINER --></div>
        </td>
        <td>&nbsp;</td>
      </tr>
    </table>
  </body>
</html>"""
    body = body.replace('edi_form_name', data.get('name'))
    body = body.replace('edi_form_strhnr', data.get('strhnr'))
    body = body.replace('edi_form_plz', data.get('plz'))
    body = body.replace('edi_form_ort', data.get('ort'))
    body = body.replace('edi_form_mail', data.get('email'))
    body = body.replace('edi_form_date', datetime.now().strftime('%d.%m.%Y %H:%M Uhr'))
    return body.encode('utf-8') 
