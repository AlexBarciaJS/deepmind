<template>
  <form>
    <md-card>

      <md-card-content>
        <div class="md-layout">
          <div class="md-layout-item md-size-100">
            <md-field maxlength="5">
              <label>Haz una pregunta</label>
              <md-textarea v-model="aboutme"></md-textarea>
            </md-field>
          </div>
          <div class="md-layout-item md-size-100 text-right">
            <md-button class="md-button md-round md-just-icon md-twitter">
              <i class="fa fa-paper-plane" aria-hidden="true"></i>
            </md-button>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </form>
</template>
<script>
export default {
  name: "chat-form",
  props: {
    dataBackgroundColor: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      aboutme:
        "",
    };
  },
};
</script>
<style></style>
