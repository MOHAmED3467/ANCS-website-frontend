<script setup>
const pdfUrl = '/ANCS-graduation-book.pdf'
</script>

<template>
  <section class="book-viewer">
    <div class="viewer-header">
      <div>
        <h1>ANCS Graduation Book</h1>
        <p>View the graduation book directly in your browser without downloading it.</p>
      </div>
      <router-link to="/" class="btn secondary">Back to Home</router-link>
    </div>

    <div class="book-frame">
      <iframe
        :src="pdfUrl"
        class="book-iframe"
        frameborder="0"
        allowfullscreen
        title="ANCS Graduation Book"
      ></iframe>
      <div class="book-fallback">
        <p>If the document does not appear above, open it directly or download it:</p>
        <p>
          <a :href="pdfUrl" target="_blank" rel="noopener" class="btn primary">Open in New Tab</a>
          <a :href="pdfUrl" download class="btn secondary">Download PDF</a>
        </p>
      </div>
    </div>

    <div class="book-viewer-actions">
      <a :href="pdfUrl" target="_blank" rel="noopener" class="btn primary">Open in New Tab</a>
      <a :href="pdfUrl" download class="btn secondary">Download PDF</a>
    </div>
  </section>
</template>

<style scoped>
.book-viewer {
  min-height: calc(100vh - 100px);
  padding: 60px 20px 80px;
  max-width: 1200px;
  margin: 0 auto;
}
.viewer-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}
.viewer-header h1 {
  margin: 0 0 10px;
  font-size: clamp(28px, 4vw, 42px);
}
.viewer-header p {
  margin: 0;
  color: var(--text-muted, #cbd5e1);
  max-width: 700px;
}
.book-iframe {
  width: 100%;
  min-height: 80vh;
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 18px;
  background: #000;
}
.book-viewer-actions {
  display: flex;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
  margin-top: 20px;
}
</style>
