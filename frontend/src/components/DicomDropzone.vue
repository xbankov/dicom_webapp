<template>
  <div class="dropzone" :class="{ 'drag-over': isDragOver }" @dragover="handleDragOver" @dragleave="handleDragLeave" @drop="handleDrop" @click="handleClick">
    <div v-if="!file">
      <p>Drag and drop a DICOM file here or click to upload</p>
    </div>
    <div v-else>
      <p>File: {{ file.name }}</p>
    </div>
    <input type="file" ref="fileInput" style="display: none" @change="handleFileSelected" accept=".dcm" />
  </div>
</template>

<script>
export default {
  name: 'DicomDropzone',
  data() {
    return {
      isDragOver: false,
      file: null,
    };
  },
  methods: {
    handleDragOver(event) {
      event.preventDefault();
      this.isDragOver = true;
    },
    handleDragLeave(event) {
      event.preventDefault();
      this.isDragOver = false;
    },
    handleDrop(event) {
      event.preventDefault();
      this.isDragOver = false;
      const file = event.dataTransfer.files[0];
      this.file = file;
      this.$emit('file-dropped', file);
    },
    handleClick() {
      this.$refs.fileInput.click();
    },
    handleFileSelected(event) {
      const file = event.target.files[0];
      this.file = file;
      this.$emit('file-dropped', file);
    },
  },
};
</script>

<style scoped>
.dropzone {
  border: 2px dashed #ccc;
  padding: 20px;
  text-align: center;
  cursor: pointer;
}

.drag-over {
  background-color: #f0f0f0;
}
</style>