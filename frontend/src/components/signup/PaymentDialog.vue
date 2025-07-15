<template>
  <el-dialog
    :v-model="visible"
    :title="title"
    width="400px"
    center
  >
    <div class="payment-content">
      <div class="payment-info">
        <div class="payment-item">
          <span>项目：</span>
          <strong>{{ item }}</strong>
        </div>
        <div class="payment-item">
          <span>金额：</span>
          <strong class="payment-amount">¥{{ amount }}</strong>
        </div>
      </div>

      <div class="payment-methods">
        <h4>选择支付方式</h4>
        <div class="methods-grid">
          <div
            v-for="method in methods"
            :key="method.id"
            class="method-card"
            :class="{ active: selectedMethod === method.id }"
            @click="selectMethod(method.id)"
          >
            <i :class="method.icon"></i>
            <span>{{ method.name }}</span>
          </div>
        </div>
      </div>

      <el-button
        type="primary"
        class="confirm-payment"
        :disabled="!selectedMethod"
        @click="confirmPayment"
      >
        确认支付
      </el-button>
    </div>
  </el-dialog>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  visible: Boolean,
  title: String,
  item: String,
  amount: Number,
  methods: Array
})

const emit = defineEmits([
  'update:visible',
  'payment-confirmed'
])

const selectedMethod = ref('')

const selectMethod = (methodId) => {
  selectedMethod.value = methodId
}

const confirmPayment = () => {
  emit('payment-confirmed', selectedMethod.value)
  closeDialog()
}

const closeDialog = () => {
  emit('update:visible', false)
  selectedMethod.value = ''
}
</script>

<style scoped>
.payment-content {
  padding: 0 20px;
}

.payment-info {
  background: rgba(15, 23, 42, 0.5);
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 25px;
}

.payment-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 12px;
  font-size: 1rem;
}

.payment-item:last-child {
  margin-bottom: 0;
}

.payment-amount {
  color: var(--secondary);
  font-size: 1.2rem;
}

.payment-methods h4 {
  margin-bottom: 15px;
  color: white;
  font-weight: 500;
}

.methods-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 15px;
  margin-bottom: 25px;
}

.method-card {
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 15px;
  text-align: center;
  cursor: pointer;
  transition: var(--transition);
}

.method-card:hover {
  border-color: var(--primary);
  background: rgba(93, 95, 239, 0.1);
}

.method-card.active {
  border-color: var(--primary);
  background: rgba(93, 95, 239, 0.2);
  box-shadow: 0 0 10px rgba(93, 95, 239, 0.2);
}

.method-card i {
  font-size: 32px;
  display: block;
  margin-bottom: 8px;
  color: var(--primary);
}

.method-card span {
  font-size: 0.9rem;
}

.confirm-payment {
  width: 100%;
  padding: 15px;
  font-size: 1rem;
  font-weight: 600;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  border: none;
}

@media (max-width: 992px) {
  .methods-grid {
    grid-template-columns: 1fr;
  }
}
</style>