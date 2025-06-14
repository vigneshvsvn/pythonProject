<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/">
    <html>
      <body>
        <h2>Product Info</h2>
        <ul>
          <li>Name: <xsl:value-of select="product/name"/></li>
          <li>Price: <xsl:value-of select="product/price"/></li>
        </ul>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>