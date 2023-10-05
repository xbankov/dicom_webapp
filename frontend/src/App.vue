<template>
  <div>
    <h1>Medical Imaging Coding Assessment</h1>
    <DicomDropzone @file-dropped="handleFileDropped" />
    <div>
      <p>Number of pixels above threshold: {{ this.volume }}</p>
    </div>
  </div>
</template>

<script>
import DicomDropzone from "./components/DicomDropzone.vue";

export default {
  name: "App",
  components: {
    DicomDropzone,
  },
  data() {
    return {
      volume: 0,
    };
  },

  methods: {
    async handleFileDropped(file) {
      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await fetch("http://localhost:8000/upload/", {
          method: "POST",
          body: formData,
        });

        const data = await response.json();

        this.volume = data.volume_mm3;
        console.log("Received Volume:", data.volume_mm3);
      } catch (error) {
        console.error("Error uploading and processing DICOM:", error);
      }
    },
  },
};
</script>
