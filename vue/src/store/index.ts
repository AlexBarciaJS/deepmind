import { defineStore } from 'pinia';

export const useMainStore = defineStore('main', {
  state: () => ({
    counter: 0,
    chatMessage: '',
    messages: [] as { id: number; question: string; response: string }[]
  }),
  actions: {
    increment() {
      this.counter++;
    },
    setChatMessage(message: string) {
      this.chatMessage = message;
    },
    addMessage(message: { id: number; question: string; response: string }) {
      this.messages.push(message);
    }
  }
});