<!-- This example requires Tailwind CSS v2.0+ -->
<template>
	<Disclosure as="nav" class="bg-gray-800" v-slot="{ open }">
		<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
			<div class="flex items-center justify-between h-16">
				<div class="flex items-center">
					<div class="hidden sm:block sm:ml-6">
						<div class="flex space-x-4">
							<!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
							<router-link to="/" v-slot="{ href, route, navigate, isActive }">
								<a
									:href="href"
									:class="[
										`px-3
										py-2
										rounded-md
										text-sm
										font-medium`,
										isActive
											? 'bg-gray-900 text-white'
											: 'text-gray-300 hover:bg-gray-700 hover:text-white',
									]"
									>Dashboard</a
								>
							</router-link>
							<router-link
								to="/purchases"
								v-slot="{ href, route, navigate, isActive }"
							>
								<a
									:href="href"
									:class="[
										`px-3
										py-2
										rounded-md
										text-sm
										font-medium`,
										isActive
											? 'bg-gray-900 text-white'
											: 'text-gray-300 hover:bg-gray-700 hover:text-white',
									]"
									>My Purchases</a
								>
							</router-link>
						</div>
					</div>
				</div>
				<div class="hidden sm:ml-6 sm:block">
					<div class="flex items-center">
						<!-- Profile dropdown -->
						<Menu v-if="$auth.isLoggedIn" as="div" class="ml-3 relative">
							<div>
								<MenuButton
									class="
										bg-gray-800
										flex
										text-sm
										rounded-full
										focus:outline-none
										focus:ring-2
										focus:ring-offset-2
										focus:ring-offset-gray-800
										focus:ring-white
									"
								>
									<span class="sr-only">Open user menu</span>
									<img
										class="h-8 w-8 rounded-full"
										src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
										alt=""
									/>
								</MenuButton>
							</div>
							<transition
								enter-active-class="transition ease-out duration-100"
								enter-from-class="transform opacity-0 scale-95"
								enter-to-class="transform opacity-100 scale-100"
								leave-active-class="transition ease-in duration-75"
								leave-from-class="transform opacity-100 scale-100"
								leave-to-class="transform opacity-0 scale-95"
							>
								<MenuItems
									class="
										origin-top-right
										absolute
										right-0
										mt-2
										w-48
										rounded-md
										shadow-lg
										py-1
										bg-white
										ring-1 ring-black ring-opacity-5
										focus:outline-none
									"
								>
									<MenuItem v-slot="{ active }">
										<a
											href="#"
											:class="[
												active ? 'bg-gray-100' : '',
												'block px-4 py-2 text-sm text-gray-700',
											]"
											>Settings</a
										>
									</MenuItem>
									<MenuItem v-slot="{ active }">
										<a
											v-if="$auth.isLoggedIn"
											@click="$auth.logout()"
											:class="[
												active ? 'bg-gray-100' : '',
												'block px-4 py-2 text-sm text-gray-700 cursor-pointer',
											]"
											>Sign out</a
										>
									</MenuItem>
								</MenuItems>
							</transition>
						</Menu>

						<div v-else>
							<router-link
								to="/login"
								v-slot="{ href, route, navigate, isActive }"
							>
								<a
									:href="href"
									:class="[
										`px-3
										py-2
										rounded-md
										text-sm
										font-medium`,
										isActive
											? 'bg-gray-900 text-white'
											: 'text-gray-300 hover:bg-gray-700 hover:text-white',
									]"
									>Sign In</a
								>
							</router-link>
						</div>
					</div>
				</div>
				<div class="-mr-2 flex sm:hidden">
					<!-- Mobile menu button -->
					<DisclosureButton
						class="
							inline-flex
							items-center
							justify-center
							p-2
							rounded-md
							text-gray-400
							hover:text-white hover:bg-gray-700
							focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white
						"
					>
						<span class="sr-only">Open main menu</span>
						<MenuIcon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
						<XIcon v-else class="block h-6 w-6" aria-hidden="true" />
					</DisclosureButton>
				</div>
			</div>
		</div>

		<DisclosurePanel class="sm:hidden">
			<div class="px-2 pt-2 pb-3 space-y-1">
				<!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
				<DisclosureButton
					as="a"
					href="#"
					class="
						bg-gray-900
						text-white
						block
						px-3
						py-2
						rounded-md
						text-base
						font-medium
					"
					>Dashboard</DisclosureButton
				>
			</div>
			<div v-if="$auth.isLoggedIn" class="pt-4 pb-3 border-t border-gray-700">
				<div class="flex items-center px-5">
					<div class="shrink-0">
						<img
							class="h-10 w-10 rounded-full"
							src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
							alt=""
						/>
					</div>
					<div class="ml-3">
						<div class="text-base font-medium text-white">Tom Cook</div>
						<div class="text-sm font-medium text-gray-400">tom@example.com</div>
					</div>
					<button
						type="button"
						class="
							ml-auto
							shrink-0
							bg-gray-800
							p-1
							rounded-full
							text-gray-400
							hover:text-white
							focus:outline-none
							focus:ring-2
							focus:ring-offset-2
							focus:ring-offset-gray-800
							focus:ring-white
						"
					>
						<span class="sr-only">View notifications</span>
						<BellIcon class="h-6 w-6" aria-hidden="true" />
					</button>
				</div>
				<div class="mt-3 px-2 space-y-1">
					<DisclosureButton
						as="a"
						href="#"
						class="
							block
							px-3
							py-2
							rounded-md
							text-base
							font-medium
							text-gray-400
							hover:text-white hover:bg-gray-700
						"
						>Your Profile</DisclosureButton
					>
					<DisclosureButton
						as="a"
						href="#"
						class="
							block
							px-3
							py-2
							rounded-md
							text-base
							font-medium
							text-gray-400
							hover:text-white hover:bg-gray-700
						"
						>Settings</DisclosureButton
					>
					<DisclosureButton
						v-if="$auth.isLoggedIn"
						@click="$auth.logout()"
						class="
							block
							px-3
							py-2
							rounded-md
							text-base
							font-medium
							text-gray-400
							hover:text-white hover:bg-gray-700
						"
						>Sign out</DisclosureButton
					>
				</div>
			</div>
		</DisclosurePanel>
	</Disclosure>
</template>

<script>
import {
	Disclosure,
	DisclosureButton,
	DisclosurePanel,
	Menu,
	MenuButton,
	MenuItem,
	MenuItems,
} from '@headlessui/vue';
import { BellIcon, MenuIcon, XIcon } from '@heroicons/vue/outline';

export default {
	components: {
		Disclosure,
		DisclosureButton,
		DisclosurePanel,
		Menu,
		MenuButton,
		MenuItem,
		MenuItems,
		BellIcon,
		MenuIcon,
		XIcon,
	},
	inject: ['$auth'],
};
</script>
